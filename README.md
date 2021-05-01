# Finance Tracker / Visualizer
A financial tracker / visualization tool used to gain insights about spending habits, trends, and patterns over varying transaction periods. This project was inspired due to deficiencies in RBC's MyFinanceTracker and my interest in personal finance developed during quarantine. I collected my own personal e statements from my RBC account and used the parser function from tika a Python parsing module. Which was used to extract the contents from my credit and debit e statements. Further string parsing techniques were used to extract transaction details and stored in a csv file. After compiling the e statements into a csv file, I was able to create meaningful data visualizations. Using echarts.js a data visualization library. The application should be usable if you are a RBC client. To use this application follow the instructions outlined in the [Getting Started](#getting-started) section.
 
## Disclaimer
Due to the structure and format of RBCs debit e statements the amounts recorded in the compiled csv file for debit transactions are not as accurate as initially intended. Certain deposits and withdrawls are not recorded with their appropriate value and create inconsistencies in total debit account balances. This application should instead be used to gain insights about your personal spending habits and trends in spending based on different periods and categories.
 
## Project Outline
 
- [Project Manifest](#project-manifest)
- [Implementation](#implementation)
    - [Extracting Data](#extracting-data)
    - [Visualizing Data](#visualizing-data)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Files](#files)
    - [E Statements](#e-statements)
    - [Category json](#category-json)
        - [Categories](#categories)
        - [Customization](#customization)
    - [CSV](#files)
    - [Execution](#execution)
    - [Visualization](#visualization)
    - [Statistics](#statistics)
 
## Project Manifest
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
 
category.json
- contains a list of keywords and categories related to them. The keywords listed in this file are based on my own transaction history. This file can be customized to compile a detailed csv file tailored to your own personal transaction history. Further details on how to edit this file are outlined in the [category.json](#catgory.json) section.
 
category.py
- returns a category based on the transaction description and keywrods in the category.json file.
 
index.html
- contains the visualization portion of the application.
 
make_credit_csv.py
- creates a csv file for credit transactions only in the directory it is saved in, the name of the csv file will have the same format as a e-statement that is downloaded from your online account. The following is an example where the account account number is 12345XXXXXX6789, the first transaciton period is 2014-01-12 and last transaction period 2021-04-12 (ex: 12345XXXXXX6789-2014-01-12-2021-04-12.csv).
 
make_csv.exe
- creates a csv file called "all-transactions.csv" for all e statements files within the current directory and its subdirectories.
 
make_csv.py 
- creates csv file  for all e statements files within the current directory and its subdirectories.
 
make_debit_csv.py
- creates a csv file for debit transactions only in the directory it is saved in, the name of the csv file will have the same format as a e-statement that is downloaded from your online account. The following is an example where the account account number is 12345XXXXXX6789, the first transaciton period is 2014-01-12 and last transaction period 2021-04-12 (ex: 12345XXXXXX6789-2014-01-12-2021-04-12.csv).
 
progressbar.py
- a command line interface progress bar used to visualize the progress of the application's execution.
 
read_credit_pdf.py
- used to parse rbc credit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction
 
read_debit_pdf.py
- used to parse rbc debit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction
 
rename.py
- used to rename e statements files that were downloaded from RBC, in order to use string parsing techniques to extract the year and
start and end month of a transaction.

read_pdf.py
- contains helper functions used by read_credit_pdf.py and read_debit_pdf.py.
 
script.js
- handles the creation of visualizations and web interactions of the application used in index.html.
 
# Implementation
The following sections outline the implementation of the project. Listing different libraries and modules and how they were used in the project.

## Extracting Data
The raw contents of the e statements were extracted using **parser** from **[tika](https://github.com/chrismattmann/tika-python)** a Python module. Further string parsing techniques from Python's standard library and Python's regular expression module **[re](https://docs.python.org/3/library/re.html)** were used to extract the account number, id, date, description, category, and amount of each transaction.

### Python Libraries
- tika: https://github.com/chrismattmann/tika-python
- re: https://docs.python.org/3/library/re.html
 
## Visualizing Data
The visualization portion of this project was implemented using echarts.js a free open source JavaScript data visualization library.

### JavaScript Libraries
- echarts.js: https://echarts.apache.org/en/index.html
 
# Getting Started
To use the application follow the steps outlined in the following sections.
 
## Prerequisites
The following list outlines the requirements for this application.
 
- [Files](#files)
- [E Statements](#e-statements)
- [category.json](#category.json)
    - [Categories](#categories)
    - [Customization](#customization)
- [CSV](#csv)
- [Execution](#execution)
- [Visualization](#visualization)
 
## Files
In order to use this application you will need a folder containing copies of your RBC e statements. For further information about how the csv file is formatted and the attributes it contains or if you plan to use your own csv file continue to the [CSV](#csv) section below.
 
## E Statements
To download your RBC e statements follow the instructions outlined in the link below:
 
https://help.sportsinteraction.com/hc/en-us/articles/360001774447-RBC-Bank-Statement-Instructions

After downloading all your e statements continue to the next section.
 
## Category json
This file contains information used to assign a category to a transaction based on keywords stored in it. The following section includes a list that outlines the different categories in category.json. The categories stored in category.json are based on categories from RBC's MyFinanceTracker application. The categories listed are arbitrary and can be changed based on your own transaction history. Categories can be added or removed based on your own transaction history, examples at the end of this section show you how to add new keywords or categories or delete them.
 
## Categories
The following is a list of the categories in category.json and examples of keywords in each category. The list of keywords were collected from my own transaction history. Steps outlined in the [Customization](#customization) section show you how to add, edit, and remove keywords and categories.
 
automotive
- transactions related to automotive purchases (ex: acura, honda,...)
 
clothing
- transactions related to clothing purchases (ex: h&m,...)
 
deposit
- transactions related to deposits
 
education
- transactions related to educational purchases (ex: university,...)
 
electronics
- transactions related to electronics purchases (ex: best buy,...)
 
entertainment
- transactions related to entertainment purchases (ex: minecraft,...)
 
e transfers
- transactions related to e-transfers
 
fee
- transactions related to fee payments
 
gas
- transactions related to gas purchases (ex: 7 eleven,...)
 
general merchandise
- transactions related to general merchandise purchases (ex: amazon,...)
 
groceries
- transactions related to grocery purchases (ex: real cdn supers,...)
 
healthcare
- transactions related to healthcare transactions (ex: dental, pharmacy,...)
 
home improvement
- transactions related to home improvement transactions (ex: rona, lowes,...)
 
loans
- transactions related to loan payments
 
mobile
- transactions related to mobile payments (ex: fido, koodo,...)
 
other
- other transactions
 
personal care
- transactions related to personal care (ex: salon, hair,...)
 
restaurants
- transactions related to restaurant purchases (ex: mcdonalds,...)
 
travel
- transactions related to travel expenses (ex: airport,...)
 
utilities
- transactions related to utility expenses (ex: enmax,...)
 
## Customization
To further customize transactions based on categories from vendors or businesses you frequent edit the category.json file by simply editing the desired keyword or category. Any new keyword or category should be added based on the specificness of the keyword is in order to assign the correct category more specific keywords and categories should be added above less specific keywords or categories.
 
### Adding a new keyword to a category example:
The code below is a sample of the category.json file, in this example we insert "new value" in the restaurants category between "mcdonalds" and "nandos". When we run the program after making these changes to category.json file, any transaction description containing the keyword "new restaurants" will be assigned "restaurants" as its category.
 
    {
        ...
        "restaurants": [
            ...
            "mcdonalds",
            "new restaurant",
            "nandos",
            ...
        ]
        ...
    }
 
### Adding a new category example:
The code below is a sample of the category.json file, in this example we add a new category before the "restaurants" category. In the "new category" category we also add the keyword "something". When we execute the program with the updated changes to category.json any transaction description that contains "something" in it will be assigned the "new category" as its category.
 
    {
        ...
        "new category": [
            "something"
        ]
        "restaurants": [
            ...
            ...
        ]
        ...
    }
    
### Deleting a keyword or category example:
To remove a key word from a category or a whole category simply delete it from category.json. In this example we remove the "new restaurant" key word we added in the first example. We also remove "new category" category we had added in the previous example.
 
    {
        ...
        "restaurants": [
            ...
            "mcdonalds",
            "nandos",
            ...
        ]
        ...
    }
 
## CSV
In order to visualize your transaction data a csv file is required. My application parses RBC e statements that can be downloaded from your online account. Alternatively a csv file constructed with the same format as shown below should also be suitable as input for the visualization portion of this project. The attributes in the csv are as follows: account number, id, date, description, category, and amount.
 
account number
- The account number of the transaction.
 
id
- The id of the transaction used to cross reference transactions in e statements. For debit transactions RBC doesn't record a unique id, in order to compensate for this the uuid python module was used to create a unique id that is used to uniquely identify transactions in the visualization portion of the project.
 
date
- The date of the transaction stored in universal time coordinate (utc) format (ex: YYYY-MM-DD).
 
category
- An arbitrary list of categories based on categories from RBC's finance tracker (ex; automotive, clothing, electronics, entertainment,...).
 
amount
- The amount of the transaction, all transactions recorded for credit accounts are negative. Payments to credit accounts are handled when debit e-statements are parsed. For a debit transaction a negative amount denotes a withdrawal, a positive amount denotes a deposit. Disclaimer due to the file format and structure of RBCs debit e statements there are some inaccuracies in values recorded for some debit transactions.
 
### example.csv
 
|account|id            |date             | description         | category           | amount |
|-------|--------------|---------------- |:-------------------:|:------------------:| ------:|
|0123456|0123456123456 |2016-01-22       | amazon              | general merchandise|  00.00 |
|1111111|1111111       |2016-01-22       | superstore          | groceries          |  12.00 |
|9876543|9876543       |2016-01-22       | mcdonalds           | restaurant         |   1.00 |
 
After collecting your e statements, follow the steps in the [Execution](#execution) section below on how to run the program.
 
## Execution
To run the program download the make_csv.exe and category.json file and run it in the folder containing your RBC e statements. The following list is a high level a step by step description of the program during execution. 

1. The program recursively searches the directory where it is saved and looks for RBC e statements. 
2. The program converts the filenames of all the e-statements found from the previous step. Renamed as the following (ex: 12345XXXXXX12345-2014-Mar12-2014-Apr12 to 12345XXXXXX12345-2014-03-12-2014-04-12). This step is required for better organization and to extract the transaction period of the e-statement.
3.  The program creates a csv file "all-transactions.csv" used to store the transactions of the e statements. 
4.  Transactions are then written to the "all-transactions.csv" file. 
5.  The program finishes execution and closes the "all-transactions.csv" file. 
6.  The file should contain a comprehensive list of all your transactions from your e statements formatted according to the example.csv above.
 
### Example of successful execution:
![alt text](https://raw.githubusercontent.com/nielsontrung/financial_visualizer/main/execution.PNG "Example Execution")
    
## Visualization
After compiling the csv file from the [Execution](#execution) section, you should now be able to open the index.html file. Here, you will be able to see a visualization showing you total spending from various transaction periods and a comprehensive visualization based on your total spending and spending habits.

## Statistics
