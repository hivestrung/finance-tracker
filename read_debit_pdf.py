import os, sys
import uuid
from category import get_category
from json import dumps
from tika import parser
from re import search, match, compile

# extract content from debit e statement
def get_debit_pdf_content(path):
  fname = str(path.parents[0]) + '/' + str(path.name)
  raw = parser.from_file(fname)
  lines = raw['content'].split('\n')
  pattern = "\d+\.\d+$"
  content = ''
  for line in lines:
    line = line.lower().replace(',','').replace('$','')
    if 'your ' in line:
      continue
    elif has_month(line) or search(pattern, line) :
      content += line + '\n'
  return content

# extract the year, start, end month, and start and end month date from the file name
def get_statement_details(fname):
  details = fname.replace('.pdf','').split('-')
  account = details[0]
  year = details[1]
  start_month = details[2]
  start_date = year + '-' + start_month + '-' + details[3]
  end_month = details[5]
  end_date = year + '-' + end_month + '-' + details[6]
  return [account, year, start_month, end_month, start_date, end_date]

def get_month_num(month):
  months = {
  "jan": "01",
  "feb": "02", 
  "mar": "03", 
  "apr": "04", 
  "may": "05", 
  "jun": "06", 
  "jul": "07", 
  "aug": "08", 
  "sep": "09", 
  "oct": "10", 
  "nov": "11", 
  "dec": "12"
  }
  return months[month]


def get_month_name(month):
  months = {
    "01": "jan",
    "02": "feb",
    "03": "mar",
    "04": "apr",
    "05": "may",
    "06": "jun",
    "07": "jul",
    "08": "aug",
    "09": "sep",
    "10": "oct",
    "11": "nov",
    "12": "dec"
  }
  return months[month]

def has_month(line):
  months = [' jan ',' feb ',' mar ',' apr ',' may ',' jun ',' jul ',' aug ',' sep ',' oct ',' nov ',' dec ']
  for month in months:
    if month in line:
      return True
  return False

def iswithdrawl(description):
  withdrawl = ['transfer', 'payment', 'fee', 'withdrawl', 'purchase', 'returned']
  for i in withdrawl:
    if 'received' in description:
      return False
    elif i in description:
      return True
  return False

# def isdeposit(description):
#   deposit = ['deposit', 'received', 'ei canada']
#   for i in deposit:
#     if i in description:
#       return True
#   return False

def get_debit_data(path,f):
  content = get_debit_pdf_content(path)
  if len(content) == 0:
    return None
  else :
    fname = str(path.name)
    # used to store transactions as json objects
    data = {}
    lines = content.splitlines()
    # get statement details from fname
    statement_details = get_statement_details(fname)
    account_number = statement_details[0]
    transaction = ''
    transactions = []
    # get year start and end month from fname
    year = statement_details[1]
    month = ''
    day = ''
    date = ''
    start_date = statement_details[4]
    end_date = statement_details[5]
    # get the transaction description
    description = ''
    # get the transaction amount
    pattern = "\d+\.\d+$"
    amount = 0
    amounts = {}
    # get balance information
    opening_balance = float(lines[0].split(' ')[2])
    closing_balance = float(lines[len(lines)-1].split(' ')[2])
    # store balances 
    balances = {}
    balances[start_date] = opening_balance
    balances[end_date] = closing_balance
    balance = 0
    for line in lines:
      if 'opening balance' in line or 'closing balance' in line:
        continue
      toks = line.split(' ')
      # print (line)
      # print (description)
      # get the date
      if toks[0].isnumeric() and len(toks[0]) <=2 :
        day = toks[0]
        month = get_month_num(toks[1])
        if len(day) < 2 :
          day = '0' + day
        # get the description
        for i in range(2,len(toks)):
          if search(pattern, toks[i]) is None:
            description += toks[i] + ' '
      # get the description
      else:
        if search(pattern, line) is not None:
          for tok in toks:
            if search(pattern, tok) is None:
              description += tok + ' '
      # if no transaction amount continue
      if search(pattern,line) is None:
        continue
      # if no balance multiple transaction's
      # on transaction date
      if search(pattern,toks[len(toks)-2]) is None:
        amount = float(toks[len(toks)-1])
      else:
        amount = float(toks[len(toks)-2])
        balance = float(toks[len(toks)-1])        
      # is transaction amount withdrawl or deposit
      if iswithdrawl(description):
        amount = -amount
      date = year + '-' + month + '-' + day
      description = description.strip()
      category = get_category(description)
      transaction = account_number  + ',' + date  + ',' + description  + ',' + category + ',' + str(amount) + '\n'
      transactions.append(transaction)
      f.write(transaction)
      transaction_json = {}
      transaction_json['year'] = year
      transaction_json['month'] = month
      transaction_json['date'] = date
      transaction_json['description'] = description
      transaction_json['category'] = category
      transaction_json['amount'] = amount
      id = str(uuid.uuid4())
      data[id] = transaction_json
      # keep track of balances
      if date in balances is None and (balance != opening_balance or balance != closing_balance):
        balances[date] = balance
      else: 
        balances[date] = balance
      # keep track of amounts based on transaction date
      if date in amounts: 
        amounts[date].append(amount)
      else:
        amounts[date] = [amount]
      # reset variables
      description = ''
      transaction = ''
      amount = 0
      balance = 0
    data = dumps(data, sort_keys = True)
    amounts = dumps(amounts, sort_keys = True)
    balances = dumps(balances, sort_keys = True)
    data = [data, transactions, balances, amounts]
    return data

args = sys.argv
if len(args) == 2:
  print(get_debit_pdf_content(args[1]))