import os, json, uuid
from tika import parser
from category import get_category
from re import search
from read_pdf import get_statement_details, get_month_num, get_month_name, has_month

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
  lines = raw['content'].splitlines()
  transaction_pattern = "^(((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec))\s{1}\d{1,2}\s{1}){2}.+(\d+\.\d+){1}$"
  month_pattern = '^(jan)|^(feb)|^(mar)|^(apr)|^(may)|^(jun)|^(jul)|^(aug)|^(sep)|^(oct)|^(nov)|^(dec)'
  id_pattern = "^\d{3,}$"
  amount_pattern = "^-?(\d+.\d+)$"
  content = ''
  for line in lines:
    line = line.lower().replace(',','').replace('$','')
    if search(transaction_pattern,line):
      continue
    elif search(month_pattern,line) or search(id_pattern,line) or search(amount_pattern,line):
      content += line + '\n'
  return content

# get all transactions from credit e statement
def get_credit_data(path, f, data):
  """
  Takes a pathlib path that specifies the location of   
  Writes transactions from the e statement to f.

  @params
    path          - Required : path of the debit e statement (pathlib Path)
    f             - Required : file being written to
    dataset       - Required : json file containing yearly total spending on a category
  """
  content = get_credit_pdf_content(path)
  if content is not None:
    fname = str(path.name)
    lines = content.splitlines()
    statement_details = get_statement_details(fname)
    # regex patterns to find transaction details
    month_pattern = '(((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec))\s{1}\d{1,2}\s{1}){2}'
    id_pattern = "^\d{3,}$"
    amount_pattern = "^-?(\d+.\d+)$"
    transaction_pattern = "^(((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec))\s{1}\d{1,2}\s{1}){2}.+(\d+\.\d+){1}$"
    # transaction detail variables
    account_number = statement_details[0]
    date_info = get_statement_details(fname)
    year = date_info[1]
    month_name = ''
    month_num = ''
    day = ''
    date = ''
    id = ''
    date = ''
    description = ''
    category = ''
    amount = 0
    transaction = ''
    for line in lines:
      toks = line.split(' ')
      if search(month_pattern,line):
        month_name = toks[0]
        month_num = get_month_num(month_name)
        day = toks[1]
        date = year + '-' + month_num + '-' + day
        for i in toks[4:]:
          description += i +' '
        description = description[:-1]
        category = get_category(description)
      elif search(id_pattern,line):
        id = line
      elif search(amount_pattern,line):
        amount = -float(line)
      if amount != 0:
        if amount < 0:
          transaction = account_number + ',' + id + ',' + date + ',' + description + ',' + category + ',' + str(amount) + '\n'
          f.write(transaction)
          data['category'][category][int(year)] += amount
          data['month'][month_name][int(year)] += amount
        transaction = ''
        id = ''
        description = ''
        category = ''
        amount = 0