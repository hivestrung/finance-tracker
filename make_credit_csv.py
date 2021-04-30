import os, sys, read_credit_pdf
from re import search
from read_credit_pdf import get_credit_pdf_content, get_credit_data
from tika import parser
from progressbar import progressBar

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
csv_header = 'account number, id, date, description, category, amount\n'
csv = account_number + '-' + start_date + '-'  + end_date + '.csv'

f = open(csv,"w")
f.write(csv_header)
for fname in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
  data = get_credit_data(fname,f)
f.close()
