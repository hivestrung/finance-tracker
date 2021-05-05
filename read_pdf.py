def get_statement_details(fname):
  """
  Takes an RBC e statement file name returns statement details about
  the statement
  @params
    fname - Required : e statement file name
  @return
    account     - account number
    year        - e statement year
    start_month - e statement start month
    end_month   - e statement end month
    start_date  - e statement start date
    end_date    - e statement end date
  """
  details = fname.replace('.pdf','').split('-')
  account = details[0]
  year = details[1]
  start_month = details[2]
  start_date = year + '-' + start_month + '-' + details[3]
  end_month = details[5]
  end_date = year + '-' + end_month + '-' + details[6]
  return [account, year, start_month, end_month, start_date, end_date]

def get_month_num(month):
  """
  Takes the name of a month returns is numerical representation
  @params
    month - Required : name of the month
  @return
    num   - number of the month as a string
  """
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
  num = months[month]
  return num


def get_month_name(month):
  """
  Takes the number of a month as a string returns the name of the month
  @params
    month - Required : number of the month
  @return
    name  - name of the month as a string
  """
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
  name = months[month]
  return name

def has_month(line):
  """
  Returns bool if line has a month
  @params 
    line - Required : line in being parsed
  
  @return
    bool - True if line has a month in it False if line does not have a month in it
  """
  months = [' jan ',' feb ',' mar ',' apr ',' may ',' jun ',' jul ',' aug ',' sep ',' oct ',' nov ',' dec ']
  for month in months:
    if month in line:
      return True
  return False

def iswithdrawal(category):
  """
  Returns bool if the description is a withdrawl
  @params 
    description - Required : transaction description
  
  @return
    bool - True if the description is a withdrawl False if the description is not a withdrawl
  """
  # purchases are always negative
  notwithdrawl = ["deposit","e transfer","government","other"]
  if 'received' in category:
    return False
  for i in notwithdrawl:
    if i == category:
      return False
  return True

def validtransaction(description):
  """
  Returns bool if the description is a valid transaction
  @params 
    description - Required : transaction description
  
  @return
    bool - False if "online banking transfer", "monthly fee", "multiproduct rebate" is in  description is other wise True
  """
  notvalid = ["online banking transfer", "monthly fee", "multiproduct rebate"]
  for i in notvalid:
    if i in description:
      return False
  return True