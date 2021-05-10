import os, json, csv
from re import search
from rename_file import rename_file
from read_pdf import get_month_name
from read_credit_pdf import get_credit_data
from read_debit_pdf import get_debit_data
from pathlib import Path
from progressbar import progressBar
from stats import get_general_stats, get_stats
from table import make_table

def print_options():
  print("Choose one of the following options below:")
  print("\t(0) exit")
  print("\t(1) recursively process all e statements")
  print("\t(2) process all-transactions.csv")

def get_input():
  clear = lambda: os.system('cls')  
  while(1):
    choice = input()
    if choice == '1' or choice == '2':
      clear()
      return choice
    elif choice == '0':
      clear()
      exit(0)
    else:
      clear()
      print_options()
  
def init_data_json(keys,start_year,end_year):
  res = {}
  for key in keys:
    years = {}
    res[key] = years
    for year in range(start_year, end_year + 1):
      years[year] = 0
    res[key] = years
  return res

def prepare_data_json(start_year,end_year):
  with open('category.json') as f:
    category = json.load(f)
  months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
  data = {}
  data['category'] = init_data_json(category,start_year,end_year)
  data['month'] = init_data_json(months,start_year,end_year)
  return data

def add_transaction_id():
  with open('all-transactions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    new_csv = 'id, account, date, description, category, amount \n'
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        new_csv += str(line_count)+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+'\n'
        line_count += 1
    f = open('all-transactions.csv','w')
    f.write(new_csv)
    f.close()

def save_data_json(data):
  with open('data.json', 'w') as j:
    json.dump(data, j, ensure_ascii=False, indent=2)

def make_data_js(start_year,end_year):
  years = end_year - start_year
  months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
  f = open('data.js','w')
  f.write('var start_year = ' + str(start_year) + '\n')
  f.write('var end_year = ' + str(end_year) + '\n')
  f.write('var years = ' + str(years) + '\n')
  f.write('var months = ' + str(months) + '\n')
  f.write('var lifetime_stats = ' + str(get_general_stats()) + '\n')
  f.write('var category_stats = ' + str(get_stats('category',start_year,end_year)) + '\n')
  f.write('var month_stats = ' + str(get_stats('month',start_year,end_year)) + '\n')
  f.close()

# main
def main():
  print_options()
  choice = get_input()

  # global variables
  start_year = 0
  end_year = 0

  # recursively process all e statements
  if choice == '1':
    statement_pattern = '\d+X+\d+-20\d{2}-\d{2}-\d{2}-20\d{2}-\d{2}-\d{2}.pdf$'
    statement_paths = Path('.').rglob('*.pdf')
    statements = []

    # rename statements
    for path in statement_paths:
      if search(statement_pattern,str(path.name)):
        rename_file(path)
        statements.append(path)
    
    if len(statements) < 1:
      print('could not find any e statements...')
      os.system("pause")
      exit(0)

    start_year = int(statements[0].name.split('-')[1])
    end_year = int(statements[len(statements)-1].name.split('-')[1])
    years = []
    for i in range(start_year,end_year):
      years.append(i)

    data = prepare_data_json(start_year,end_year)

    # open statements and write to csv file
    csv_file = 'all-transactions.csv'
    csv_header = 'id, account , date, description, category, amount\n'
    f = open(csv_file,'w')
    f.write(csv_header)
    for statement in progressBar(statements, prefix = 'Progress:', suffix = 'Complete', length = 50):
      if len(statement.name) == 38:
        get_debit_data(statement,f,data)
      if len(statement.name) == 42:
        get_credit_data(statement,f,data)
    f.close()

    # give transactions an id
    add_transaction_id()
    # round amounts to two decimal places
    for i in data['category']:
      for j in data['category'][i]:
        data['category'][i][j] = round(data['category'][i][j],2)

    for i in data['month']:
      for j in data['month'][i]:
        data['month'][i][j] = round(data['month'][i][j],2)
  # process all-transactions.csv
  elif choice == '2':
    if not os.path.isfile('all-transactions.csv'):
      print('did not find all-transactions.csv')
      os.system("pause")
      exit(0)

    with open("all-transactions.csv",'r') as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=',')
      rows = list(csv_reader)
      start_year = int(rows[1][2].split('-')[0])
      end_year = int(rows[len(rows)-1][2].split('-')[0])
      data = prepare_data_json(start_year,end_year)
      line_count = 0
      year = 0
      month = ''
      amount = 0    
      for row in progressBar(rows, prefix = 'Progress:', suffix = 'Complete', length = 50):
        if line_count == 0:
          line_count += 1
        else:
          year = row[2].split('-')[0]
          month = get_month_name(row[2].split('-')[1])
          amount = float(row[5])
          data['category'][row[4]][int(year)] = amount
          data['month'][month][int(year)] = amount
          line_count += 1
  # save data to json file
  save_data_json(data)
  # prepare data.js variables for visualization
  make_data_js(start_year,end_year)
  # convert all-transactions.csv to html table
  make_table()

if __name__ == '__main__':
  main()