import os, sys, time
from re import search
from read_credit_pdf import get_credit_pdf_content, get_credit_data
from read_debit_pdf import get_debit_pdf_content, get_debit_data
from tika import parser
from progressbar import progressBar

args = sys.argv


