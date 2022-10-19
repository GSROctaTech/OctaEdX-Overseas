

import pandas as pd
#Read and write to excel
dataFileUrl = r"/Users/stutiverma/Downloads/coalpublic2012.xls"
data = pd.read_table(dataFileUrl)

'''

if WScript.Arguments.Count < 3 Then
    WScript.Echo "Please specify the source and the destination files. Usage: ExcelToCsv <xls/xlsx source file> <csv destination file> <worksheet number (starts at 1)>"
    Wscript.Quit
End If

csv_format = 6

Set objFSO = CreateObject("Scripting.FileSystemObject")

src_file = objFSO.GetAbsolutePathName(Wscript.Arguments.Item(0))
dest_file = objFSO.GetAbsolutePathName(WScript.Arguments.Item(1))
worksheet_number = CInt(WScript.Arguments.Item(2))

Dim oExcel
Set oExcel = CreateObject("Excel.Application")

Dim oBook
Set oBook = oExcel.Workbooks.Open(src_file)
oBook.Worksheets(worksheet_number).Activate

oBook.SaveAs dest_file, csv_format

oBook.Close False
oExcel.Quit

Convert the Excel XML file in CSV:
$ cscript ExcelToCsv.vbs coalpublic2012.xls coalpublic2012.csv 1

Open the CSV file with pandas
df1 = pd.read_csv('coalpublic2012.csv', skiprows=3)

'''