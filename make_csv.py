import json
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

# create dataset json that will be used in visualization 
categories = {}
with open('category.json') as f:
  categories = json.load(f)

data = {}
start_year = int(statements[0].name.split('-')[1])
end_year = int(statements[len(statements)-1].name.split('-')[1])

for c in categories:
  category = {}
  for year in range(start_year, end_year + 1):
    category[year] = 0
  data[c] = category

# open statements and write to csv file
csv = 'all-transactions.csv'
csv_header = 'account number, id, date, description, category, amount\n'
f = open(csv,'w')
f.write(csv_header)
for statement in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
  if len(statement.name) == 38:
    get_debit_data(statement,f,data)
  elif len(statement.name) == 42:
    get_credit_data(statement,f,data)
f.close()

# round amounts to two decimal places
for i in data:
  for j in data[i]:
    data[i][j] = round(data[i][j],2)

# save data to json file
with open('data.json', 'w') as j:
  json.dump(data, j, ensure_ascii=False, indent=2)
