import pandas as pd
import dask.dataframe as dd

import zipfile
import xml.etree.ElementTree as ET

# CSV, XLSX, ZIP, TXT, CSV, JSON, XML, HTML, Images, Hierarchical Data Format, PDF, DOCX

dfCSV = pd.read_csv("/home/Loan_Prediction/train.csv"")
dfXLSX = pd.read_excel("/home/Loan_Prediction/train.xlsx", sheetname="Invoice")

# Read File from Zip Files
archive = zipfile.ZipFile('T.zip', 'r')
df = archive.read('train.csv')

text_file = open("text.txt", "r")
lines = text_file.read()

# Read JSON
dfJSON = pd.read_json("/home/kunal/Downloads/Loan_Prediction/train.json")

tree = ET.parse('/home/sunilray/Desktop/2 sigma/train.xml')
root = tree.getroot()
print(root.tag)
