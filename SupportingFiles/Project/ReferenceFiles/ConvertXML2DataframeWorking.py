import pandas as pd
import xml.etree.ElementTree as et
import csv

xtree = et.parse("E:/GSReddy/PythonProjects/SampleData/employee.xml")
xroot = xtree.getroot()

df_cols = ['id','name','email','password','liveLocation']

rows = []

for node in xroot:
    s_id = node.find("id").text if node is not None else None
    s_name = node.find("name").text if node is not None else None
    s_mail = node.find("email").text if node is not None else None
    s_pwd = node.find("password").text if node is not None else None
    s_loc = node.find("liveLocation").text if node is not None else None

    rows.append({"id": s_id,
                 "name": s_name,
                 "email": s_mail,
                 "password": s_pwd,
                 "liveLocation": s_loc})

out_df = pd.DataFrame(rows, columns=df_cols)

out_df.to_csv("E:/GSReddy/PythonProjects/SampleData/xml2csv_test.csv", sep='|', index=False,header=True)