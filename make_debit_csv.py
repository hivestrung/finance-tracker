import os, sys
from re import search
from read_debit_pdf import get_debit_pdf_content, get_debit_data
from tika import parser

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
  """
  Call in a loop to create terminal progress bar
  @params:
    iteration   - Required  : current iteration (Int)
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    length      - Optional  : character length of bar (Int)
    fill        - Optional  : bar fill character (Str)
    printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
  """
  total = len(iterable)
  # Progress Bar Printing Function
  def printProgressBar (iteration):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
  # Initial Call
  printProgressBar(0)
  # Update Progress Bar
  for i, item in enumerate(iterable):
      yield item
      printProgressBar(i + 1)
  # Print New Line on Complete
  print()

args = sys.argv

if len(args) == 1:  
  files = os.listdir('.')
  
  # get files that are e statements
  e_statement_pattern = '\d+X+\d+-20\d{2}-\d{2}-\d{2}-20\d{2}-\d{2}-\d{2}.pdf'
  statements = []
  for f in files:
    if search(e_statement_pattern,f):
      statements.append(f)

  # get the account number and start and end date used for the csv name
  first_statement = statements[0].replace('.pdf','').split('-')
  last_statement = statements[len(statements)-1].replace('.pdf','').split('-')
  account_number = first_statement[0]
  start_date = first_statement[1] + '-' + first_statement[2] + '-' + first_statement[3]
  end_date = last_statement[4] + '-' + last_statement[5] + '-' + last_statement[6]

  # write transactions to csv file
  csv_header = 'account number, date, description, category, amount\n'
  csv = account_number + '-' + start_date + '-'  + end_date + '.csv'

  f = open(csv,"w")
  f.write(csv_header)
  for fname in progressBar(files, prefix = 'Progress:', suffix = 'Complete', length = 50):
    if fname.find('.pdf') != -1:
      data = get_debit_data(fname,f)
  f.close()
elif len(args) == 2:
  fname = args[1]
  f = open('test.txt','w')
  content = get_debit_pdf_content(fname)
  # print (content)
  data = get_debit_data(fname,f)
  transcations = data[0]
  for transaction in transcations:
    print (transaction)
  f.close()