from re import search
# get a category from transaction description 
# category listings are based from my own personal transaction history
def get_category(description):
  automotive = ['acura', 'auto', 'canadian tire', 'cdn tire', 'compu-care', 'mitsubishi']
  clothing = ['abercrombie', 'h&m', 'old navy', 'shoe', 'simons', 'skechers', 'sport chek', 'uniqlo', 'urban planet', 'winners', 'zara']
  deposit = ['deposit']
  education = ['cbe', 'john wiley & sons', 'quizlet', 'sait', 'u of c', 'unversity', 'vitalsource']
  electronics = ['best buy', 'logitech', 'memory', 'microsoft', 'newegg', 'source']
  entertainment = ['cineplex', 'entertainment', 'games', 'jagex', 'mojang', 'spotify', 'stampede', 'steam']
  fee = ['fee']
  gas = ['eleven', 'esso', 'gas', 'husk', 'petro', 'shell']
  general = ['aliexpress', 'amazon', 'dollar store', 'miniso', 'staples', 'wal-mart']
  groceries = ['atlantic superstore', 'bulk barn', 'co-op', 'costco', 'dominion', 'extra foods', 'farm boy', 'food basics', 'fortinos', 'freshco', 'freshmart', 'grocery', 'iga', 'loblaws', 'loeb', "longo's", 'market', 'maxi', 'metro', "mike dean's super food stores", 'no frills', 'provigo', 'quality foods', 'rabba', 'real canadian superstore', 'safeway', 'save-on-foods', 'saveeasy', 'sobeys', "steinberg's (supermarket)", 'superstore', 'thrifty foods', 'valu-mart', 'independent grocer', 'zehrs markets']
  healthcare = ['ahs', 'brunet', 'dental', 'drug', 'familiprix', 'jean coutu group', 'lawtons', 'london drugs', 'pharmachoice', 'pharmacy', 'rexall', 'shoppers drug mart']
  homeimprovement = ['lowe', 'rona', 'the home depot']
  loans = ['loan']
  mobile =  ['bell', 'fido', 'koodo', 'rogers', 'telus']
  other = ['other']
  restaurants = ['a&w', 'bbq', 'beef', 'black bull', 'brewsters', 'cafe', 'chatime', 'chef', 'chef', 'chianti', 'chicken', 'chinese', 'coco tea', 'dairy', 'deli', "denny's", 'donday', 'doordash', 'food', 'grill', 'kitchen', 'korean', 'marble', 'mcdonald', 'pho', 'pizza', 'ramen', 'restaurant', 'rotisserie', 'saigon', 'samosa', 'shawarma', 'ssome', 'sushi', 'tea', 'thai', 'vietnam', "wendy's", 'wok']
  travel = ['airport', 'bus', 'park', 'transit']
  utilities = ['cable', 'enmax', 'insurance']

  categories = {
    'automotive': automotive,
    'clothing': clothing,
    'deposit': deposit,
    'education': education,
    'electronics': electronics,
    'entertainment': entertainment,
    'fee': fee,
    'gas': gas,
    'general merchandise': general,
    'groceries': groceries,
    'healthcare': healthcare,
    'home improvement': homeimprovement,
    'loans': loans,
    'mobile': mobile,
    'other': other,
    'restaurants': restaurants,
    'travel': travel,
    'utilities': utilities
  }  

  category = ''
  for i in categories:
    for j in categories[i]:
      if search(j, description):
        category = i
        return category
  category = 'other'  
  return category