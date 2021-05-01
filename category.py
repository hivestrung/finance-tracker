import json
from re import search

# get a category from transaction description 
# category listings are based from my own personal transaction history
def get_category(description):
  categories = []
  with open('category.json') as f:
    categories = json.load(f)

  category = ''
  for i in categories:
    for j in categories[i]:
      if search(j, description):
        category = i
        return category
  category = 'other'  
  return category

get_category('description')