# Finance Tracker / Visualizer
A financial tracker / visualization tool used to gain insights about spending habits, trends, and patterns over varying transaction periods. This project was inspired due to deficiencies in RBC's Finance Tracker and my interest in personal finance developed during quarantine. I collected my own personal e statements from my RBC account and used **parser** a Python text parsing module. Which was used to extract the contents from my credit and debit e statements. Further string parsing techniques were used to extract transaction details and stored in a csv file. After compiling the e statements into a csv file, I was able to create meaningful visualizations using echarts.js, data visualization library. The application should be usable if you are also a RBC client. To use this application follow the instructions outlined in the [Getting Started](#getting-started) section.
 
## Disclaimer
 
Due to the structuring and format of RBCs debit e statements the amounts recorded in the compiled csv file for debit transactions are not as accurate as initially intended. And creates inconsistencies in total balances. This application should instead be used to gain insights about your personal spending habits and trends in spending based on different periods and categories.
 
## Project Outline
 
- [Project Manifest](#project-manifest)
- [Implementation](#implementation)
    - [Extracting Data](#extracting-data)
    - [Visualizing Data](#visualizing-data)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Files](#files)
    - [E Statements](#e-statements)
    - [category.json](#category.json)
        - [Categories](#categories)
        - [Customization](#customization)
    - [CSV](#files)
    - [Execution](#execution)
    - [Visualization](#visualization)
 
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
- contains a list of categories and keywords related to them, based on my own transaction history. This file can be customized to compile a detailed csv file tailored to your own personal transaction history.
 
category.py
- returns a category based on the transaction description and based on the data in the category.json file.
 
index.html
- contains the web based portion of the application.
 
make_credit_csv.py
- used to create the csv file for credit transactions only.
 
make_csv.exe
- creates a csv file for all e statements files within the current directory and its subdirectories.
 
make_csv.py: creates csv file  for all e statements files within the current directory and its subdirectories.
 
make_debit_csv.py
- used to create a csv file for debit transactions only.
 
progressbar.py
- is a command line interface progress bar used to visualize the progress of the application's execution.
 
read_credit_pdf.py
- used to parse rbc credit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction
 
read_debit_pdf.py
- used to parse rbc debit e-statements. Used to extract the transaction date, posting date, transaction id, business details, and the amount of the transaction
 
rename.py
- used to rename e statements files that were downloaded from RBC, in order to use string parsing techniques to extract the year and
start and end month of a transaction.
 
script.js
- handles the creation of visualizations and web interactions of the application.
 
# Implementation
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
In order to use this application you will need a folder containing copies of your RBC e statements or your own csv file properly formatted according to the example in the [CSV](#csv) section. For further information about how the csv file will be compiled continue to the [CSV](#csv) section below.
 
## E Statements
To download your RBC e statements follow the instructions outlined in the link below:
 
https://help.sportsinteraction.com/hc/en-us/articles/360001774447-RBC-Bank-Statement-Instructions
 
To further understand how the csv file is structured and what data it includes continue to the [CSV](#csv) section.
 
## category.json
This file contains information used to assign a category to a transaction based on keywords stored in the category.json file. The list below outlines the different categories in category.json. The categories stored in category.json are based on categories used in RBC's MyFinanceTracker application. The categories listed are arbitrary values and can be changed freely based on your own transaction history. Categories can be added or removed based on your own transaction history. Examples at the end of this section show you how to add new key words or categories.
 
## Categories
The following is a list of the categories in category.json and examples of keywords in each category. Steps outlined in the [Customization](#customization) section show you how to add, edit, and remove keywords and categories.
 
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
To further customize transactions based on categories from vendors or businesses you frequent edit the category.json file by simply adding or removing the keyword or category. Any new keyword or category should be added alphabetically for organization and maintenance.
 
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
 
To remove a key word from a category or a whole category simply delete it from category.json. In this example we remove the "new restaurant" key word we added in the first example. We also remove the "new category" category we had added in the previous example.
 
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
In order to visualize your financial data a csv file is required. My application is able to parse RBC e statements that can be downloaded from your online account. Alternatively a csv file constructed with the same format as shown below should also be suitable as input for the visualization portion of this project. The attributes in the csv are as follows: account number, id, date, description, category, and amount.
 
account number
- The account number of the transaction.
 
id
- The id of the transaction used to cross reference transactions in e statements. For debit transactions RBC doesn't record a unique id, in order to compensate for this the uuid python module was used to create a unique id that is used to uniquely identify transactions in the visualization portion of the project.
 
date
- The date of the transaction stored in universal time coordinate (utc) format (ex: YYYY-MM-DD).
 
category
- An arbitrary list of categories used in RBC's finance tracker (ex; automotive, clothing, electronics, entertainment,...). Categories can be customized by editing the category.json file as mentioned in the [category.json](#category.json) section. To create a more personalized csv file based on your own transaction history.
 
amount
- The amount of the transaction, a negative transaction amount denotes a purchase on a credit transaction, on a debit transaction a negative amount denotes a withdrawal. Disclaimer due to the file format and structure of RBCs debit e statements there are some inaccuracies in values recorded for some debit transactions.
 
example.csv
 
|account|id            |date             | description         | category           | amount |
|-------|--------------|---------------- |:-------------------:|:------------------:| ------:|
|0123456|0123456123456 |2016-01-22       | amazon              | general merchandise|  00.00 |
|1111111|1111111       |2016-01-22       | superstore          | groceries          |  12.00 |
|9876543|9876543       |2016-01-22       | mcdonalds           | restaurant         |   1.00 |
 
After collecting your e statements, follow the steps in the [Execution](#execution) section below on how to run the program.
 
## Execution
To run the program download the make_csv.exe and category.json file and run it in the folder containing your RBC e statements. The application recursively searches the current directory where it is saved and looks for RBC e statements. After the program finishes executing, there should be a csv file called "all-transactions". This file should contain a comprehensive list of all your transactions from your e statements formatted according to the example.csv above. As previously mentioned in the [File Manifest](#file-manifest) section and the [CSV](#csv) section, category.json can be edited to match certain based on your own spending. To see how to edit category.json continue to the [category.json](#category.json) section below.
 
An example of the application completing execution:
 
![alt text](https://raw.githubusercontent.com/nielsontrung/financial_visualizer/main/execution.PNG "Example Execution")
    
## Visualization
After compiling the csv file from the [Execution](#execution) section, you should now be able to open the index.html file. Here, you will be able to see a visualization showing you total spending from various transaction periods and a comprehensive visualization based on your total spending and spending habits.
