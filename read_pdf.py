import os
from tika import parser
# extract text from estatment
fname = './451029XXXXXX6910-2016-01-12-2016-02-12.pdf'
account = 
raw = parser.from_file(fname)
content = raw['content']
lines = content.splitlines()
# store all transactions
transactions = []
# used to store purchases
purchase = ''
purchases = []
total_purchases = 0
purchase_amount = 0
purchase_amounts = []
# find payment transactions
thank_you = 'PAYMENT - THANK YOU / PAIEMENT - MERCI'
payment = ''
payments = []
total_payments = 0
payment_amount = 0
payment_amounts = []
for line in lines:
  # find payments
  if line.find(thank_you) != -1:
    payment += line + ' '
  elif payment.find(thank_you) != -1 and line.find('-$') != -1:
    payment += line
    payments.append(payment)
    transactions.append(payment)
    payment = ''
    payment_amount = float(line.replace('$',''))
    payment_amounts.append(payment_amount)
    total_payments += payment_amount
  # find purchases
  elif (line.find("JAN") == 0 or line.find("FEB") == 0) and line.find("$") != -1:
    purchase += line
    purchases.append(purchase)
    transactions.append(purchase)
    purchase = ''
    purchase_amount = float(line[line.find('$'):len(line)].replace('$',''))
    purchase_amounts.append(purchase_amount)
    total_purchases += purchase_amount
  elif line.find("JAN") == 0 or line.find("FEB") == 0:
    purchase += line + ' '
  elif (purchase.find("JAN") != -1 or purchase.find("FEB") != -1):
    if line.find('$') != -1:
      purchase += line
      purchases.append(purchase)
      transactions.append(purchase)
      purchase = ''
      purchase_amount = float(line.replace('$',''))
      purchase_amounts.append(purchase_amount)
      total_purchases += purchase_amount
      
  
# write to a new file
out_file = fname.replace("pdf","txt")
f = open(out_file,"w")

for transaction in transactions:
  f.write(transaction + '\n')

# for transaction in purchases:
#   f.write(transaction+'\n')

# for transaction in payments:
#   f.write(transaction+'\n')

f.close()

# write pdf content to raw.txt
f = open('raw.txt','w')
f.write(content)
f.close()
print("total transactions")
print(len(transactions))
print("number of purchases")
print(len(purchases))
print("number of payments")
print(len(payments))
print("total purchases")
print(total_purchases)
for amount in purchase_amounts:
  print(' ' + str(amount))
print("total payments")
print(total_payments)
for amount in payment_amounts:
  print(' ' + str(amount))

print(total_purchases + total_payments)