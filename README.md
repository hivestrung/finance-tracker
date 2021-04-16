# Financial Visualizer

A financial visualization tool used to see trends and patterns over varying transcation periods. I collected my own personal e statements from RBC's and used **parser** a python module, which was used extract the contents from the e statements. Further string parsing techniques were used to extract transaction details into a csv file format. After compiling the e statments into a csv file I was able to create data visualizations using chart.js. The following application should also executable if you are also an RBC client. To see your own transaction history follow the instructions outlined in the "Getting Started" header.

- [Getting Started](#getting-started)
- [Implementation](#implementation)
- [File Manifest](#file-manifest)
## Getting Started
#### Prerequisites
To execute the python files an installation of python is required. Download link to python with instructions can be found in the link proved below.
- https://www.python.org/downloads/
After installing python, rename.py and read_pdf.py should be executable following the command

To rename e statements files with the following filename f

    python ./rename.py
    
## Implementation
#### Extracting Data
The following python module was used to extract the raw contents from e statments. which was then processed further using python string methods and formatted to a csv file.

- parser https://docs.python.org/3/library/parser.html

#### Extracting Data
The following library was used to implement visualize the data.

- chart.js

## File Manifest
- rename.py
- read_pdf.py
