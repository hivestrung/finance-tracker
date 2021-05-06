def make_table():
  # begin the table
  table = ''
  table += "<table id='table' class='table table-sm table-dark table-striped'>"

  infile = open("all-transactions.csv","r")
  i = 0
  for line in infile:
    row = line.replace('&','').split(",")
    account = row[0]
    id = row [1]
    date = row[2]
    description = row[3]
    category = row[4]
    amount = row[5]
    if i == 0:
      # column headers
      table += "<thead>"
      table += "<tr>"
      table += "<div><th>%s</th></div>" % account
      table += "<div><th>%s</th></div>" % id
      table += "<div><th>%s</th></div>" % date
      table += "<div><th>%s</th></div>" % description
      table += "<div><th>%s</th></div>" % category
      table += "<div><th>%s</th></div>" % amount
      table += "</tr>"
      table += "</thead>"
      table += "<tbody>"
    else:
      # entries
      table += "<tr>"
      table += "<td>%s</td>" % account
      table += "<td>%s</td>" % id
      table += "<td>%s</td>" % date
      table += "<td>%s</td>" % description
      table += "<td>%s</td>" % category
      table += "<td>%s</td>" % amount
      table += "</tr>"
    i = 1
  table.replace('\n',' ')

  # end the table
  table += "</tbody>"
  table += "</table>"
  f = open('table.js','w')
  f.write("var table = \"" + table.replace('\n',' ') + "\"")
  f.close()