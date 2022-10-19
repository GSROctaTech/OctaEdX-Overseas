import sqlite3
import pandas as pd

conn = sqlite3.connect('../itemdb')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS items
          ([item_id] INTEGER PRIMARY KEY, [item_name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([item_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')

c.execute('''
          INSERT INTO items (item_id, item_name)
                VALUES
                (1,'Microwave'),
                (2,'Oven'),
                (3,'Refrigerator'),
                (4,'Toaster'),
                (5,'Blender')
          ''')

c.execute('''
          INSERT INTO prices (item_id, price)
                VALUES
                (1,250),
                (2,700),
                (3,1200),
                (4,80),
                (5,300)
          ''')

conn.commit()

c.execute('''
          SELECT
          a.item_name,
          b.price
          FROM items a
          LEFT JOIN prices b ON a.item_id = b.item_id
          ''')

df = pd.DataFrame(c.fetchall(), columns = ['item_name','price'])
print (df)