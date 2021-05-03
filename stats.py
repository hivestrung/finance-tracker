import json
# get some basic statistics from data.json
# total expenses per category
# total expenses per year
# category with the most purchases
# number of transactions per category
# average transaction amount per category
# monthly spending
# average monthly spending
def get_general_stats():
  with open('data.json') as f:
    data = json.load(f)
  years = len(data['category']['deposit'])
  category_data = data['category']
  # get total and average spending per category
  stats = []
  earnings = 0
  spendings = 0
  for i in category_data:
    for j in category_data[i]:
      if category_data[i][j] > 0:
        earnings += category_data[i][j]
      elif category_data[i][j] < 0:
        spendings += category_data[i][j]
  stats.append(round(earnings,2))
  stats.append(round(earnings/years,2))
  stats.append(round(spendings,2))
  stats.append(round(spendings/years,2))
  return stats

def get_stats(key):
  with open('data.json') as f:
    data = json.load(f)
  if key == 'category':
    years = len(data[key]['deposit'])
    data = data['category']
  elif key == 'month':
    years = len(data[key]['jan'])
    data = data['month']
  piedata = []
  bardata = []  
  for key in data:
    total = 0
    monthlydata = []
    for amount in data[key]:
      total += data[key][amount]
      monthlydata.append(data[key][amount])
    total = round(total,2)
    average = round(total/years,2)
    piedata.append([key,total,average])
    bardata.append([key,monthlydata])
  return [piedata,bardata]