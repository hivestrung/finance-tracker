# Finance Tracker / Visualizer
A financial tracker / visualization tool used to gain insights about spending habits, trends, and patterns over varying transcation periods. This project was inspired due to deficiencies in RBC's Finance Tracker and my developed interest in personal finance during quarantine. I collected my own personal e statements from my RBC account and used **parser** a Python text parsing module. Which was used extract the contents from my credit and debit e statements. Further string parsing techniques were used to extract transaction details and stored in a csv file. After compiling the e statements into a csv file, I was able to create meaningful visualizations using echarts.js. A comprehensive data visualization library. The following application should be usable if you are also a RBC client. To use this application and see a comprehensive csv of your own transaction history follow the instructions outlined in the "Getting Started" section. The following application can be downloaded and run locally.

- [File Manifest](#file-manifest)
- [Implementation](#implementation)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Files](#files)
        - [E Statements](#e-statements)
        - [CSV](#files)
    - [Execution](#execution)
    - [Visualization](#visualization)

## File Manifest
The following list and descriptions are file specifications and details about each file and their functionality in the project.

- index.html
- progressbar.py
- rename.py
- read_credit_pdf.py
- read_debit_pdf.py
- script.js

index.html contains the web based portion of the application.

progressbar.py is a commanline interface progress bar used to visualize the progress of the applications execution. 

rename.py is a simple python script used to rename e statements files that were downloaded from RBC, in order to use string parsing techniques to extract the year and 
start and end month of a transaction.

read_credit_pdf.py is a python script that is used to parse rbc credit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction

read_debit_pdf.py is a python script that is used to parse rbc debit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction

script.js handles the creation of visualizations and web interactions of the application.

## Implementation
The financial visualizer tool was implemented as previously mentioned in the project summary with parser and chart.js
### Extracting Data
The following python module was used to extract the raw contents from e statements. which was then processed further using python string methods and formatted to a csv file.

- parser https://docs.python.org/3/library/parser.html

### Visualizing Data
The following library was used to implement visualize the data.

- chart.js

## Getting Started
### Prerequisites
The following list outlines the requirements for this application. 

- [Files](#files)
    - [E Statements](#e-statements)
    - [CSV](#csv)
- [Tools](#tools)
- [Execution](#execution)
### Files
In order to use this application you will need copies of your e statements or your own csv. If you are a RBC client continue to the "Files" section, if you plan to use your own csv file then continue to the "CSV" section.

#### E Statements
Your e statements are stored digitally in your RBC account, which can be accessed by following these instructions:

After downloading all of your e statements continue to the "Tools" section.

#### CSV
The data visualization tool is also able to take a csv file as input, to use your own csv file follow the format according to the table below. The attributes required in the csv are as follows account, transaction date, type of transaction, category, and amount. The in the table below are as listed below. After creating your csv file continue to the "Tools" section.

- Account Number
    - the account number 
- Transaction ID
    - the id of the transaction used to cross reference transaction in e statement
- Transaction Date
    - the date of the transaction
    - must be in universal time coordinate (utc) format ex: YYYY-MM-DD
- Posting Date
    - the date the transaction was executed
    - must be in universal time coordinate (utc) format ex: YYYY-MM-DD
- Category: an arbitrary list of categories used in RBC's finance tracker
    - utilities
    - entertainment
    - health
    - groceries
    - transportation
    - electronics
- Amount
    - the amount of the transaction, a negative transaction amount denotes a purchase on a credit transaction, on a debit transaction a negavtive amount denotes a withdraw

example.csv

|Account|Transaction ID|Transaction Date | Description         | Category           | Amount |
|-------|--------------|---------------- |:-------------------:|:------------------:| ------:|
|0123456|0123456123456 |2016-01-22       | amazon              | general merchandise| $00.00 |
|1111111|1111111       |2016-01-22       | superstore          | groceries          | $12.00 |
|9876543|9876543       |2016-01-22       | mcdonalds           | restaurant         |  $1.00 |

After collecting your e statements, follow the steps below to run the program.

### Execution

Download the make_csv.exe file and run it in a folder containing all of your e statements. After the program finishes executing, there should be a csv file called "all-transactions". This file should contain a comprehensive list of all your transactions from your e statements formatted according to the csv example above.
    
### Visualization
After completing the steps from the Execution section you should now have a properly formatted csv file.
