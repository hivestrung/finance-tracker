from re import search
from rename_file import rename_file
from read_credit_pdf import get_credit_data
from read_debit_pdf import get_debit_data
from pathlib import Path
from progressbar import progressBar

statement_pattern = '\d+X+\d+-20\d{2}-\d{2}-\d{2}-20\d{2}-\d{2}-\d{2}.pdf$'
statement_paths = Path('.').rglob('*.pdf')
statements = []

# rename statements
for path in statement_paths:
  rename_file(path)
  if search(statement_pattern,str(path.name)):
    statements.append(path)

# open statements and write to csv file
csv = 'all-transactions.csv'
csv_header = 'account number, id, date, description, category, amount\n'
f = open(csv,'w')
f.write(csv_header)
for statement in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
  if len(statement.name) == 38:
    get_debit_data(statement,f)
  elif len(statement.name) == 42:
    get_credit_data(statement,f)
f.close()