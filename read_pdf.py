# extract the year, start, end month, and start and end month date from the file name
def get_statement_details(fname):
  details = fname.replace('.pdf','').split('-')
  account = details[0]
  year = details[1]
  start_month = details[2]
  start_date = year + '-' + start_month + '-' + details[3]
  end_month = details[5]
  end_date = year + '-' + end_month + '-' + details[6]
  return [account, year, start_month, end_month, start_date, end_date]

def get_month_num(month):
  months = {
  "jan": "01",
  "feb": "02", 
  "mar": "03", 
  "apr": "04", 
  "may": "05", 
  "jun": "06", 
  "jul": "07", 
  "aug": "08", 
  "sep": "09", 
  "oct": "10", 
  "nov": "11", 
  "dec": "12"
  }
  return months[month]


def get_month_name(month):
  months = {
    "01": "jan",
    "02": "feb",
    "03": "mar",
    "04": "apr",
    "05": "may",
    "06": "jun",
    "07": "jul",
    "08": "aug",
    "09": "sep",
    "10": "oct",
    "11": "nov",
    "12": "dec"
  }
  return months[month]

def has_month(line):
  months = [' jan ',' feb ',' mar ',' apr ',' may ',' jun ',' jul ',' aug ',' sep ',' oct ',' nov ',' dec ']
  for month in months:
    if month in line:
      return True
  return False

def iswithdrawl(description):
  withdrawl = ['transfer', 'payment', 'fee', 'withdrawl', 'purchase', 'returned']
  for i in withdrawl:
    if 'received' in description:
      return False
    elif i in description:
      return True
  return False