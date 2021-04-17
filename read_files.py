import read_pdf, os, sys
from tika import parser

files = os.listdir('.')

fname = 'all-transactions.pdf'

# prepare file names for csv and txt file
csv_file = fname.replace("pdf","csv")
txt_file = fname.replace("pdf","txt")
# open files for writing
f = open(csv_file,"w")
t = open(txt_file,"w")

for file in files:
  get_data(f,t,year,start_month,end_month,lines)

f.close()
t.close()