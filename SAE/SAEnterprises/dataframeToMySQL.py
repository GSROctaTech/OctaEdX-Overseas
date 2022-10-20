# import pymysql
# from pandas.io import sql
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="root",
#                                pw="your_password",
#                                db="octaedx"))
# df.to_sql(con=engine, name='APPLICANT', if_exists='replace')

import sqlalchemy
import pandas as pd
import numpy as np
import pymysql

database_username = 'root'
database_password = ''
database_ip = 'localhost'
database_name = 'octaedx'

np.random.seed(0)
number_of_samples = 10
frame = pd.DataFrame({
    'feature1': np.random.random(number_of_samples),
    'feature2': np.random.random(number_of_samples),
    'class': np.random.binomial(2, 0.1, size=number_of_samples),
}, columns=['feature1', 'feature2', 'class'])

print(frame)

database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                      database_ip, database_name))
frame.to_sql(con=database_connection, name='MySQLTable', if_exists='replace')
