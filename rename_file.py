import os
import sys

# print(sys.argv)

# if len(sys.argv) == 2:
    
fnames = os.listdir('.')

l = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

months = {
"Jan": "-01-",
"Feb": "-02-",
"Mar": "-03-",
"Apr": "-04-",
"May": "-05-",
"Jun": "-06-",
"Jul": "-07-",
"Aug": "-08-",
"Sep": "-09-",
"Oct": "-10-",
"Nov": "-11-",
"Dec": "-12-"
}

# s = "451029XXXXXX6910-2016Dec13-2017Jan12.pdf"
# print(s.replace("Dec",months["Dec"]))
s = ''
for fname in fnames:
  s = fname
  print(s)
  for month in l:
    if s.find(month) != -1:
      s = s.replace(month, months[month])
  print(s)
  os.rename(fname, s)
