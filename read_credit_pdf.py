import os, json
from tika import parser
from category import get_category
from read_pdf import get_statement_details, get_month_num, get_month_name

# extract text from estatment
def get_credit_pdf_content(path):
  """
  Takes a pathlib path that specifies the location of 
  a debit e statement returns the contents of specified file.

  @params
    path    - Required : path of the debit e statement (pathlib Path)

  @return
    content - transactions of the debit e statement
  """
  fname = str(path.parents[0]) + '/' + str(path.name)
  raw = parser.from_file(fname)
  content = raw['content']
  return content

# get all transactions from credit e statement
def get_credit_data(path, f, dataset):
  """
  Takes a pathlib path that specifies the location of 
  a debit e statement returns the contents of specified file.

  @params
    path          - Required : path of the debit e statement (pathlib Path)
    f             - Required : file being written to
    dataset       - Required : json file containing yearly total spending on a category
  @return
    transactions  - list of transactions as csv row
    amounts       - list of amounts->float
  """
  content = get_credit_pdf_content(path)
  if content is not None:
    fname = str(path.name)
    lines = content.splitlines()
    statement_details = get_statement_details(fname)
    # get account number from the file name
    account_number = statement_details[0] + ','
    # get year and month of transaction
    date_info = get_statement_details(fname)
    year = date_info[1]
    start_month = date_info[2]
    end_month = date_info[3]
    start_month_name = get_month_name(start_month)
    end_month_name = get_month_name(end_month)
    # maintenance transactions
    maintenance_transactions = []
    maintenance_amounts = []
    # 
    id = 0
    ids = []
    # keep track of transaction date
    date = ''
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
        temp = line.replace(start_month_name+' ', year +'-' + start_month + '-')
        temp = temp.replace(end_month_name+' ', year + '-' + end_month + '-')
        # get transaction and posting date
        date = temp[:10]
        # get business/vendor description of transaction
        description = line[14:].replace(',', ' ')
        # get category based on description of transaction
        category = get_category(description)
      # get the transaction id
      elif line.isnumeric():
        id = line
        ids.append(id)        
      # get transaction amount
      elif (date.find(start_month) != -1 or date.find(end_month) != -1):
        if line.find('$') != -1:        
          amount = line.replace("$",'')
          if amount.find(','):
            amount = amount.replace(',', '')
          amount = float(amount)*-1
          amounts.append(amount)
          transaction = account_number  + ',' + id  + ',' + date  + ',' + description  + ',' + category  + ',' + str(amount) + '\n'
          transactions.append(transaction)
          if amount < 0:
            f.write(transaction)
            dataset[category][int(year)] += amount
          transaction = ''
          date = ''
          description = ''
          category = ''
    data = [transactions, amounts]
  return data