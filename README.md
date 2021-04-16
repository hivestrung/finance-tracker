# Financial Visualizer
## Summary
A financial visualization tool used to see insights, trends, and patterns over varying transcation periods. This project was inspired due to limitations and inaccuracies in RBC's Finance Tracker. I collected my own personal e statements from RBC's and used **parser** a python module, which was used extract the contents from the e statements. Further string parsing techniques were used to extract transaction details into a csv file format. After compiling the e statments into a csv file I was able to create data visualizations using chart.js. The following application should also be executable if you are also an RBC client or create your own csv file. To use this application and see your own transaction history follow the instructions outlined in the "Getting Started" section. The following application can be downloaded and run locally.

- [File Manifest](#file-manifest)
- [Implementation](#implementation)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Files](#files)
    - [CSV](#files)


## File Manifest
rename.py is a simple python script used to rename e statment files that were downloaded from RBC.

read_pdf.py is another python script that was used to parse transaction details extracted from the estatements.

index.html contains the web based portion of the application.

script.js handles the creation of visualizations and web interactions of the application.
- rename.py
- read_pdf.py
- index.html
- script.js

## Implementation
The financial visualizer tool was implemented as previously mentioned in the project summary with parser and chart.js
### Extracting Data
The following python module was used to extract the raw contents from e statments. which was then processed further using python string methods and formatted to a csv file.

- parser https://docs.python.org/3/library/parser.html

### Visualizing Data
The following library was used to implement visualize the data.

- chart.js

## Getting Started
### Prerequisites
The following list outlines the requirements for this application. 

- [Files](#files)
    - [E Statments](#e-statments)
    - [CSV](#csv)
- [Tools](#tools)
- [Execution](#execution)
#### Files
In order to use this application you will need copies of your e statments or your own csv. If you are a RBC client continue to the "Files" section, if you plan to use your own csv file then continue to the "CSV" section.

##### E Statments
Your e statements are stored digitally in your RBC account, which can be accessed by following these instructions:
- df
- df
- df

After downloading all of your e statments continue to the "Tools" section.

##### CSV
The data visualization tool is also able to take a csv file as input, to use your own csv file follow the format according to the table below. The attributes required in the csv are as follows account, transaction date, type of transaction, category, and amount. The in the table below are as listed below. After creating your csv file continue to the "Tools" section.

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

### Tools
To execute the python files an installation of python is required. If you do not have a installation of python follow the download link, installation instructions are also provided by the link.
- https://www.python.org/downloads/

After installing python, rename.py and read_pdf.py should be executable, to execute the scripts follow the instructions below:

### Execution

To rename e statements run the following command in command prompt:
This is important in order to extract the transaction date from the pdf files.

    python ./rename.py path\to\your\e\statements
    
After executing this command your e statments should be renamed from the following .pdf to .pdf.
Following this step run the command in command prompt:

    python ./read_pdf.py path\to\your\e\statements

After executing this command there should now be a text file containing all your transaction history,
compiled from all of your e statments.

