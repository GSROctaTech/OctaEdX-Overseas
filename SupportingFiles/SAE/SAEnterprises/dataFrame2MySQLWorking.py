import pandas as pd
import pymysql
from sqlalchemy import create_engine
import numpy as np

user = 'root'
passw = ''
host = 'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address
port = 3306
database = 'octaedx'

mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database,
                     echo=False)

# Pull Data from an CSV file
# directory = r'directoryLocation'  # path of csv file
# csvFileName = 'something.csv'
# df = pd.read_csv(os.path.join(directory, csvFileName ))

# Random Data Generation, for testing insert
np.random.seed(0)
number_of_samples = 10
df = pd.DataFrame({
    'feature1': np.random.random(number_of_samples),
    'feature2': np.random.random(number_of_samples),
    'class': np.random.binomial(2, 0.1, size=number_of_samples),
}, columns=['feature1', 'feature2', 'class'])
print("Dataframe Data")
print(df)

df.to_sql(name='mysqltable',  # name=csvFileName[:-4],
          con=mydb,
          if_exists='replace', index=False)

data = pd.read_sql('SELECT * FROM octaedx.mysqltable', mydb)
print("Fetched Data From Table")
print(data)

"""
if_exists: {'fail', 'replace', 'append'}, default 'fail'
     fail: If table exists, do nothing.
     replace: If table exists, drop it, recreate it, and insert data.
     append: If table exists, insert data. Create if does not exist.
"""
