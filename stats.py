import json
# get some basic statistics from data.json
# total expenses per category
# total expenses per year
# category with the most purchases
# number of transactions per category
# average transaction amount per category
# monthly spending
# average monthly spending
def get_category_stats():
  with open('data.json') as f:
    data = json.load(f)

  stats = {}
  years = len(data['category']['deposit'])
  print (years)
  category_data = data['category']
  stats['category'] = {}
  for i in category_data:
    total = 0
    for j in category_data[i]:
      total += category_data[i][j]
    stats['category']['total'] = round(total,2)
    stats['category']['average'] = round(total,2)

  month_data = data['month']

  # print (data['month'])
  # dictionary used to store stats about data
  # stats = {}

#   # get the total spending for each category

# # def get_month_stats():

print("total and average yearly spending per category")
get_category_stats()