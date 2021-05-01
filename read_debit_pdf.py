import os, sys
import uuid
from category import get_category
from json import dumps
from tika import parser
from re import search
from read_pdf import get_statement_details, get_month_num, get_month_name, has_month, iswithdrawal, validtransaction

# extract content from debit e statement
def get_debit_pdf_content(path):
  """
  Takes a pathlib path that specifies the location of 
  a debit e statement returns the contents of specified file.

  @params
    path  - Required : path of the debit e statement (pathlib Path)

  @return
    content - transactions of the debit e statement
  """
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

def get_debit_data(path,f,dataset):
  """
  Takes a pathlib path that specifies the location of 
  a debit e statement returns the contents of specified file.

  @params
    path          - Required : path of the debit e statement (pathlib Path)
    f             - Required : file being written to
    dataset       - Required : json file containing yearly total spending on a category
  @return
    data          - list containing transactions of the debit e statement as json objects
    transactions  - list of transactions as csv row
    balances      - dictionary of balances {date:balance}
    amounts       - dictionary of amounts {date:amount}
  """
  content = get_debit_pdf_content(path)
  if len(content) == 0:
    return None
  else :
    fname = str(path.name)
    # used to store transactions as json objects
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
      # create transation csv row
      id = str(uuid.uuid4())      
      date = year + '-' + month + '-' + day
      description = description.strip()
      category = get_category(description)
      ### determine if amount is positive or negative ###
      # received transacitons are always positive
      if 'received' in description:
        amount = abs(amount)
      elif 'purchase' in description:
        amount = -abs(amount)
      # transactions on certain categories will always be negative
      elif iswithdrawal(category):
        amount = -abs(amount)
      if 'deposit' in category:
        amount = abs(amount)
      transaction = account_number + ',' + id  + ',' + date  + ',' + description  + ',' + category + ',' + str(amount) + '\n'
      # online banking transfer transactions are payments 
      # to visa account will not be included in the csv
      # monthly fees and monthly rebates will not be included
      if validtransaction(description):
        transactions.append(transaction)
        f.write(transaction)
        # create transaction json object
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
        dataset[category][int(year)] += amount
      # reset variables after every transaction
      description = ''
      transaction = ''
      amount = 0
      balance = 0
    amounts = dumps(amounts, sort_keys = True)
    balances = dumps(balances, sort_keys = True)
    data = [transactions, balances, amounts]
    return data
