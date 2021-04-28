import os, json
from tika import parser
from category import get_category

# extract text from estatment
def get_credit_pdf_content(fname):
  raw = parser.from_file(fname)
  content = raw['content']
  return content

# extract the year, start month, and end month from the file name
def get_statement_details(fname):
  details = fname.split('-')
  account = details[0]
  year = details[1]
  start_month = details[2]
  end_month = details[5]
  return [account, year, start_month, end_month]

def get_month_name(month):
  months ={
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

# get all transactions from credit e statement
def get_credit_data(fname, f):
  content = get_credit_pdf_content(fname)
  if content is not None:
    lines = content.splitlines()
    statement_details = get_statement_details(fname)
    # prepare json data
    data = {}
    # get account number from the file name
    account_number = statement_details[0] + ','
    # get year and month of transaction
    year_months = get_statement_details(fname)
    year = year_months[1]
    start_month = year_months[2]
    end_month = year_months[3]
    start_month_name = get_month_name(start_month)
    end_month_name = get_month_name(end_month)
    # maintenance transactions
    maintenance_transactions = []
    maintenance_amounts = []
    # 
    id = 0
    ids = []
    # keep track of transaction date
    transaction_date = ''
    # used to create the csv string
    transaction = ''
    transactions = []
    # get the transaction description
    description = ''
    # get the category based on description
    category = ''
    # keep track of transaction amounts
    amount = 0
    amounts = []
    # find payment transactions
    for line in lines:
      line = line.lower()
      # get maintenance transactions
      if (line.find(start_month_name) == 0 or line.find(end_month_name) == 0) and line.find("$") != -1:
        amount = line.replace("$",'')
        amounts.append(amount)
        transaction += amount
        maintenance_transactions.append(transaction)
        transaction = ''
        amount = float(line[line.find('$'):len(line)].replace('$',''))
        maintenance_amounts.append(amount)
      # get transaction dates and business
      elif line.find(start_month_name) == 0 or line.find(end_month_name) == 0:
        # convert date to utc format
        temp = line.replace(start_month_name+' ', year+'-'+start_month+'-')
        temp = temp.replace(end_month_name+' ', year+'-'+end_month+'-')
        # get transaction and posting date
        transaction_date = temp[:10] + ','
        # get business/vendor description of transaction
        description = line[14:].replace(',', ' ') + ','
        # get category based on description of transaction
        category = get_category(description) + ','
      # get the transaction id
      elif line.isnumeric():
        id = line + ','
        ids.append(id)        
      # get transaction amount
      elif (transaction_date.find(start_month) != -1 or transaction_date.find(end_month) != -1):
        if line.find('$') != -1:        
          amount = line.replace("$",'')
          if amount.find(','):
            amount = amount.replace(',', '')
          amount = float(amount)*-1
          amounts.append(amount)
          transaction = account_number + id + transaction_date + description + category + str(amount) + '\n'
          transactions.append(transaction)
          if amount < 0:
            f.write(transaction)
          transaction = ''
          transaction_date = ''
          description = ''
          category = ''
    data = [transactions, amounts]
  return data