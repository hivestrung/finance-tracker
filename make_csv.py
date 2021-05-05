import json
from re import search
from rename_file import rename_file
from read_credit_pdf import get_credit_data
from read_debit_pdf import get_debit_data
from pathlib import Path
from progressbar import progressBar
from stats import get_general_stats, get_stats
from table import make_table

def make_data(keys,start_year,end_year):
  res = {}
  for key in keys:
    years = {}
    res[key] = years
    for year in range(start_year, end_year + 1):
      years[year] = 0
    res[key] = years
  return res

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
years = []
for i in range(start_year,end_year):
  years.append(i)

data = {}
data['category'] = make_data(category,start_year,end_year)

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
data['month'] = make_data(months,start_year,end_year)

# open statements and write to csv file
csv = 'all-transactions.csv'
csv_header = 'id, account , date, description, category, amount\n'
f = open(csv,'w')
f.write(csv_header)
for statement in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
  if len(statement.name) == 38:
    get_debit_data(statement,f,data)
  if len(statement.name) == 42:
    get_credit_data(statement,f,data)
f.close()

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

# write data to data.js for visualization
f = open('data.js','w')
f.write('var start_year = ' + str(start_year) + '\n')
f.write('var end_year = ' + str(end_year) + '\n')
f.write('var years = ' + str(years) + '\n')
f.write('var months = ' + str(months) + '\n')
f.write('var lifetime_stats = ' + str(get_general_stats()) + '\n')
f.write('var category_stats = ' + str(get_stats('category',start_year,end_year)) + '\n')
f.write('var month_stats = ' + str(get_stats('month',start_year,end_year)) + '\n')
f.close()
# convert the csv to html table
make_table()