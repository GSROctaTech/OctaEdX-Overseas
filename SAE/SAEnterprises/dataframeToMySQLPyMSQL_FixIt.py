import pymysql

user = 'root'
passw = ''
host = 'localhost'
port = 3306
database = 'octaedx'

# If you already have the database created:

conn = pymysql.connect(host=host,
                       port=port,
                       user=user,
                       passwd=passw,
                       db=database,
                       charset='utf8')

data.to_sql(name=database, con=conn, if_exists='replace', index=False, flavor='mysql')

# ---------------- If you do NOT have the database created, also valid when the database is already there  ----------
conn = pymysql.connect(host=host, port=port, user=user, passwd=passw)

conn.cursor().execute("CREATE DATABASE IF NOT EXISTS {0} ".format(database))
conn = pymysql.connect(host=host,
                       port=port,
                       user=user,
                       passwd=passw,
                       db=database,
                       charset='utf8')

data.to_sql(name=database, con=conn, if_exists='replace', index=False, flavor='mysql')
