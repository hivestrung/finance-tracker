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

def get_stats(key,start_year,end_year):
  """
  @params 
  """
  with open('data.json') as f:
    data = json.load(f)
  if key == 'category':
    years = len(data[key]['deposit'])
    data = data[key]
  elif key == 'month':
    years = len(data[key]['jan'])
    data = data[key]
  total_stats = []
  yearly_stats = []
  # get lifetime total and average spending per category
  # get yearly total spending per category
  for i in data:
    total = 0
    yearlydata = []
    yearlydata.append(i)
    for amount in data[i]:
      total += data[i][amount]
      yearlydata.append(abs(data[i][amount]))
    total = round(total,2)
    average = round(total/years,2)
    total_stats.append([i,total,average])
    yearly_stats.append(yearlydata)
  if key == 'category':
    # yearly spending for every category
    yearly_data = []
    for year in range(start_year,end_year+1):
      temp = []
      for i in data:
        if i == 'deposit' or i == 'other' or i == 'government':
          continue
        else:
          temp.append(abs(data[i][str(year)]))
      temp.reverse()
      yearly_data.append([str(year),temp])
    res = [total_stats,yearly_stats,yearly_data]
    return res
  else:
    # yearly spending for month category
    yearly_data = []
    for year in range(start_year,end_year+1):
      temp = []
      for i in data:
        if i == 'deposit' or i == 'other' or i == 'government':
          continue
        else:
          temp.append(abs(data[i][str(year)]))
      # temp.reverse
      yearly_data.append([str(year),temp])
    res = [total_stats,yearly_stats,yearly_data]
    return res
# print(get_stats('category',2014,2021)[2])
# print(get_stats('month',2014,2021)[2])