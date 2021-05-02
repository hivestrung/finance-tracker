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
data = {}
with open('category.json') as f:
  category = json.load(f)

start_year = int(statements[0].name.split('-')[1])
end_year = int(statements[len(statements)-1].name.split('-')[1])

data = {}
dic = {}
years = {}

for c in category:
  dic[c] = years
  for year in range(start_year, end_year + 1):
    years[year] = 0
  dic[c] = years
data['category'] = dic
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
dic = {}

years = {}
for m in months:
  dic[m] = years
  for year in range(start_year, end_year + 1):
    years[year] = 0
  dic[m] = years
data['month'] = dic

# open statements and write to csv file
csv = 'all-transactions.csv'
csv_header = 'account number, id, date, description, category, amount\n'
f = open(csv,'w')
f.write(csv_header)
# for statement in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
for statement in statements:
  print (statement.name)
  if len(statement.name) == 38:
    get_debit_data(statement,f,data)
  if len(statement.name) == 42:
    get_credit_data(statement,f,data)
f.close()

data['month']['jan'][2014] = 10

# round amounts to two decimal places
for i in data['category']:
  for j in data['category'][i]:
    data['category'][i][j] = round(data['category'][i][j],2)

for i in data['month']:
  for j in data['month'][i]:
    data['month'][i][j] = round(data['month'][i][j],2)

# save data to json file
with open('data.json', 'w') as j:
  json.dump(data, j, ensure_ascii=False, indent=2)
