# Finance Tracker / Visualizer
A financial tracker / visualization tool used to gain insights about spending habits, trends, and patterns over varying transcation periods. This project was inspired due to deficiencies in RBC's Finance Tracker and my interest in personal finance developed during quarantine. I collected my own personal e statements from my RBC account and used **parser** a Python text parsing module. Which was used extract the contents from my credit and debit e statements. Further string parsing techniques were used to extract transaction details and stored in a csv file. After compiling the e statements into a csv file, I was able to create meaningful visualizations using echarts.js, data visualization library. The application should be usable if you are also a RBC client. To use this application follow the instructions outlined in the [Getting Started](#getting-started) section. 

## Disclaimer

Due to the structuring and format of RBC's debit e statements the amounts recorded in the compiled csv file for debit transactions are not as accurate as initially intended. And creates inconsistencies in total balances. This application is instead intended to see insights in spending habits and trends in spending based on different periods and categories.

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
The following is a list of files used in the project and a description of each file.

- category.json
- category.py
- index.html
- make_credit_csv.py
- make_csv.exe
- make_csv.py
- make_debit.csv
- progressbar.py
- read_credit_pdf.py
- read_debit_pdf.py
- rename_file.py
- script.js

**category.json** a json file containing a list of categories and key words related to them, based on my own transaction history. This file can be customized to compile a detailed csv file tailored to your own personal transaction history.

**category.py** returns a category based on the transaction description and based on the data in the category.json file.

**index.html** contains the web based portion of the application.

**progressbar.py** is a commanline interface progress bar used to visualize the progress of the applications execution. 

**rename.py** is a simple python script used to rename e statements files that were downloaded from RBC, in order to use string parsing techniques to extract the year and 
start and end month of a transaction.

**read_credit_pdf.py** is a python script that is used to parse rbc credit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction

**read_debit_pdf.py** is a python script that is used to parse rbc debit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction

**script.js** handles the creation of visualizations and web interactions of the application.

## Implementation

The financial visualizer tool was implemented as previously mentioned in the project summary with parser and echarts.js

### Extracting Data
The raw contents of the e statements were extracted using **parser** from **[tika](https://github.com/chrismattmann/tika-python)** a Python module. Further string parsing techniques from Python's standard library and Python's regular expression module **[re](https://docs.python.org/3/library/re.html)** were used to extract the account number, id, date, description, category, and amount of each transaction that was extracted from the e statement. Python's standard.

- tika: https://github.com/chrismattmann/tika-python
- re: https://docs.python.org/3/library/re.html

### Visualizing Data
The following library was used to visualize the data.

- echarts.js

## Getting Started
### Prerequisites
The following list outlines the requirements for this application. 

- [Files](#files)
    - [E Statements](#e-statements)
    - [CSV](#csv)
- [Tools](#tools)
- [Execution](#execution)
### Files
In order to use this application you will a folder containing copies of your e statements or your own csv file properly formatted according to the example in the [CSV](#csv) section. If you are a RBC client continue to the [Files](#files) section. For further information about how the csv file that will be compiled is structure continue to the [CSV](#csv) section below. If not skip to the [Execution](#execution) section. If you plan to use your own csv file then continue to the [CSV](#csv) section.

#### E Statements
Your e statements are stored digitally in your RBC account, which can be accessed by following the instructions outlined in the link below:

https://help.sportsinteraction.com/hc/en-us/articles/360001774447-RBC-Bank-Statement-Instructions

After downloading all of your e statements continue to the [Execution](#execution) section.

#### CSV
The data visualization tool is also able to take a csv file as input, to use your own csv file follow the format according to the table below. The attributes required in the csv are as follows account, transaction date, type of transaction, category, and amount. The in the table below are as listed below. After creating your csv file continue to the [Execution](#execution) section.

- account number: the account number 
- id: the id of the transaction used to cross reference transaction in e statement
- date: the date of the transaction must be in universal time coordinate (utc) format ex: YYYY-MM-DD the date the transaction was executed must be in universal time coordinate (utc) format ex: YYYY-MM-DD
- Category: an arbitrary list of categories used in RBC's finance tracker (ex; automotive, clothing, electronics, entertainment,...) categories can be customized by editing the category.json file as mentioned in the [File Manifest](#file-manifest) section to gain a more personalized csv file based on your own transaction history.
- Amount: the amount of the transaction, a negative transaction amount denotes a purchase on a credit transaction, on a debit transaction a negavtive amount denotes a withdraw. Disclaimer due to the file format and structure of RBC's debit e statements there are inaccurracies in values recorded for some debit transactions.

example.csv

|account|id            |date             | description         | category           | amount |
|-------|--------------|---------------- |:-------------------:|:------------------:| ------:|
|0123456|0123456123456 |2016-01-22       | amazon              | general merchandise|  00.00 |
|1111111|1111111       |2016-01-22       | superstore          | groceries          |  12.00 |
|9876543|9876543       |2016-01-22       | mcdonalds           | restaurant         |   1.00 |

After collecting your e statements, follow the steps in the [Execution](#execution) section below on how to run the program.

### Execution
Download the make_csv.exe and category.json file and run it in the folder containing all of your e statements. The application recursively searches the current directory where it is saved and looks for e statements. After the program finishes executing, there should be a csv file called "all-transactions". This file should contain a comprehensive list of all your transactions from your e statements formatted according to the csv example above. As previously mentioned in the [File Manifest](#file-manifest) section and the [CSV](#csv) section.
    
### Visualization
After compiling the csv file from the [Execution](#execution) section, you should now be able to open the index.html file. Here, you will be able to see a visualization showing you total spending from various transaction periods and a comprehensive visualization based on your total spending and spending habits.
