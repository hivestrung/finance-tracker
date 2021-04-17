import os, json
from tika import parser
# extract text from estatment
fname = './451029XXXXXX6910-2016-01-12-2016-02-12.pdf'
# extract the date from the file name
i = fname.find('-')
account = fname[2:i]
year = fname[i+1:i+5]
i = fname.find(year+'-')+5
start_month = fname[i:i+2]
i = fname.rfind(year+'-')+5
end_month = fname[i:i+2]
  
raw = parser.from_file(fname)
content = raw['content']
# write pdf content to raw.txt
f = open('raw.txt','w')
f.write(content)
f.close()
lines = content.splitlines()

def remove_all_occurrences(s,old,new):
  temp = s
  while temp.find(old) >= 0:
    temp = s.replace(old, new)
  return temp

def get_category(business):

  category = ''
  return category

def get_data(f,t,lines):
  f.write('id, transaction date, posting date, business, amount\n')
  t.write('id, transaction date, posting date, business, amount\n')  
  # prepare json data
  data = {}
  # maintenance transactions
  maintenance_transactions = []
  maintenance_amounts = []
  # 
  id = 0
  ids = []
  # keep track of transaction date
  transaction_date = ''
  transaction_dates = []
  # keep track of posting dates
  posting_date = ''
  posting_dates = []
  # used to create the csv string
  transaction = ''
  transactions = []
  # get the transaction details
  business = ''
  businesses = []
  # keep track of transaction amounts
  amount = 0
  amounts = []
  # find payment transactions
  for line in lines:
    # get maintenance transactions
    if (line.find("JAN") == 0 or line.find("FEB") == 0) and line.find("$") != -1:
      date = line[:13]
      amount = line.replace("$",'')
      amounts.append(amount)
      transaction += amount
      maintenance_transactions.append(transaction)
      transaction = ''
      amount = float(line[line.find('$'):len(line)].replace('$',''))
      maintenance_amounts.append(amount)
    # get transaction dates and business
    elif line.find("JAN") == 0 or line.find("FEB") == 0:
      # convert date to utc format
      temp = remove_all_occurrences(line, "JAN ",year+'-'+start_month+'-')
      temp = remove_all_occurrences(temp, "FEB ",year+'-'+end_month+'-')
      # get transaction and posting date
      transaction_date = temp[:10] + ','
      posting_date = temp[11:21] + ','
      # get business/vendor of transaction
      business = line[14:] + ','
      businesses.append(business)
      # create the csv format string
      transaction = transaction_date + posting_date + business
      business = ''    
    elif line.isnumeric():
      id = line + ','
      ids.append(id)
      transaction = id + transaction
    # get transaction amount
    elif (transaction.find(start_month) != -1 or transaction.find(end_month) != -1):
      if line.find('$') != -1:        
        amount = line.replace("$",'')        
        transaction += amount + '\n'
        transactions.append(transaction)
        f.write(transaction)
        t.write(transaction)
        transaction = ''
        # get the amount as a float
        amount = float(amount)
        amounts.append(amount)
  data = [transactions, businesses, amounts]
  return data
# prepare file names for csv and txt file
csv_file = fname.replace("pdf","csv")
txt_file = fname.replace("pdf","txt")
# open files for writing
f = open(csv_file,"w")
t = open(txt_file,"w")
data = get_data(f,t,lines)
f.close()
t.close()
