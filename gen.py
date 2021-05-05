import json
from random import choice,uniform
from category import get_category

def gen_random_transactions():
  # generate random transaction history
  f = open('example.csv','w')
  descriptions = ["acura","auto","canadian tire","cdn tire","compu-care","megatire","mitsubishi","sudsy's","abercrombie","denim","h&m","old navy","shoe","simons","skechers","sport chek","uniqlo","urban planet","value village","vanity","winners","zara","cbe","john wiley & sons","quizlet","resume","sait","u of c","unversity","vitalsource","best buy","logitech","memory","microsoft","newegg","source","bacchus","cineplex","entertainment","games","jagex","minecraft","mojang","spotify","stampede","steam","e-transfer","fine payment","fee","item returned","eleven","esso","gas","highway","husk","mobil@","petro","shell","aliexpress","amazon","dollar store","miniso","staples","wal-mart","canada revenue","citizenship","ei canada","government","gst canada","payment canada","tax refund","atlantic superstore","bulk barn","co-op","costco","dominion","extra foods","farm boy","food basics","fortinos","freshco","freshmart","grocery","iga","loblaws","loeb","longo's","market","maxi","metro","mike dean's super food stores","no frills","provigo","quality foods","quickly","rabba","real cdn","real canadian superstore","safeway","save-on-foods","saveeasy","sobeys","steinberg's (supermarket)","superstore","thrifty foods","valu-mart","independent grocer","zehrs markets","ahs","brunet","dental","drug","dr.","familiprix","jean coutu group","lawtons","lens","london drugs","pharmachoice","pharmacy","rexall","shoppers drug mart","lowe","rona","south peak","the home depot","investment","questrade","special deposit","loan","bell","fido","koodo","rogers","telus","other","cut","hair","nail","protein","salon","spa","a&w","barcelos","bbq","beef","black bull","bobby","breakfast","brewsters","cafe","chatime","chef","chianti","chicken","chinese","coco tea","crunchy","dairy","deli","denny's","donday","doordash","dynasty","five guys","food","grey eagle","grill","huong","irish","kebab","kitchen","korean","mango","manrijangsung","marble","mcdonald","moxie's","nando's","pho","pizza","ramen","restaurant","rotisserie","saigon","saltlik","samosa","shawarma","ssome","sushi","tea","thai","vietnam","wendy's","wok","airport","bus","park","transit","aviva","cable","enmax","insurance","cash","withdrawal","transfer to deposit","deposit"]
  years = ['2014','2015','2016','2017','2018','2019']
  months = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
  days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
  id = 0
  account = '12345XXX67890'
  date = ''
  description = ''
  category = ''
  amount = 0
  transaction = ''
  for year in years:
    for month in months:
      # generate 10 random transactions for every month
      for i in range(10):
        day = choice(days)
        date = year + '-' + month + '-' + day
        description = choice(descriptions)
        category = get_category(description)
        amount = round(uniform(1.00,1000.00),2)
        id +=1
        transaction = str(id) + ',' + account + ',' + date + ',' + description + ',' + category + ',' + str(amount) + '\n'
        f.write(transaction)
  f.close()

gen_random_transactions()