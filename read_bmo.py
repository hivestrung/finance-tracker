import os
from tika import parser
from re import search
from category import get_category

directory = os.listdir('.')
f = open('bmo.csv','w')
for i in directory:
  if 'eStatement' in i:
    raw = parser.from_file(i)
    lines = raw['content'].lower().splitlines()
    month_pattern = '^((jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec))\..+(\d+\.\d+)$'
    amount_pattern = "(\d+.\d+)$"
    content = ''
    for line in lines:
      if search(month_pattern, line):
        content += line + '\n'
    lines = content.splitlines()
    for line in lines:
      toks = line.split(' ')
      month = toks[0]
      day = toks[1]
      date = ''
      date = month + '-' + day
      description = ''
      for i in toks[5:-1]:
        description += i + ' '
      category = get_category(description)
      amount = float(toks[-1])
      transaction = date + ',' + description + ',' + category + ',' + str(amount) + '\n'
      f.write(transaction)
      transaction = ''
      description = ''
      categories = ''
      amount = 0
f.close()