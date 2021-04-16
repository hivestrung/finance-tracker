# Financial Visualizer

A financial visualization tool used to see insights, trends, and patterns over varying transcation periods. I collected my own personal e statements from RBC's and used **parser** a python module, which was used extract the contents from the e statements. Further string parsing techniques were used to extract transaction details into a csv file format. After compiling the e statments into a csv file I was able to create data visualizations using chart.js. The following application should also be executable if you are also an RBC client or create your own csv file. To use this application and see your own transaction history follow the instructions outlined in the "Getting Started" section.

- [File Manifest](#file-manifest)
- [Implementation](#implementation)
- [Getting Started](#getting-started)


## File Manifest
rename.py is a simple python script used to rename e statment files that were downloaded from RBC.

read_pdf.py is another python script that was used to parse transaction details extracted from the estatements.
- rename.py
- read_pdf.py

## Implementation
The financial visualizer tool was implemented as previously mentioned in the project summary with parser and chart.js
#### Extracting Data
The following python module was used to extract the raw contents from e statments. which was then processed further using python string methods and formatted to a csv file.

- parser https://docs.python.org/3/library/parser.html

#### Visualizing Data
The following library was used to implement visualize the data.

- chart.js

## Getting Started
#### Prerequisites
In order to use this application you will need a copy of e statments or your own csv. If you are a RBC client continue to the "Files" section, if you plan to use your own csv file then continue to the "CSV Format" section.
- [](#Files)
#####
#### Files
e statments or a csv file will be required in order to create your own visualization, if you have your own csv file make sure it is properly formatted as specified below you.


#### CSV Format
The data visualization tool is also able to take a csv file as input, to use your own csv file follow the format according to the table below. The attributes displayed in the table below are as listed below.

- Transaction Date
    - must be in universal time coordinate (utc) format ex: YYYY-MM-DD
- Type of Transaction
    - transactions are either payments or purchases 
- Category
    - utilities
    - entertainment
    - health
    - groceries
    - 

example.csv

|Account| Transaction Date | Type of Transaction | Category | Amount |
|-------| ---------------- |:-------------------:|:--------:| ------:|
|0123456| 2016-01-22       | "purchase"          | $00.00   | $00.00 |
|1111111| 2016-01-22       | "payment"           | $12.00   | $12.00 |
|9876543| 2016-01-22       | "payment"           |  $1.00   |  $1.00 |

After collecting your e statments 

#### Tools
To execute the python files an installation of python is required. Download link to python with instructions can be found in the link proved below.
- https://www.python.org/downloads/
After installing python, rename.py and read_pdf.py should be executable following the command

To rename e statements files with the following filename f

    python ./rename.py
    



