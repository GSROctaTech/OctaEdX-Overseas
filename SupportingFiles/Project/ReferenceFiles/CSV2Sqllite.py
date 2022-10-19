import pandas as pd
from sqlalchemy import create_engine
import os, glob

# create sqlalchemy db connetion
engine = create_engine('sqlite:///data.sqlite', echo=True)
sqlite_connection = engine.connect()

# get current working directory path
# get list of files in current working directory
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

for file in csv_files:
    # get the filename (e.g. 'C:\\Users\\{currently logged in user}\\Desktop\\folder_with_files\\fileName.csv' => 'fileName.csv')
    dataFileName = file.split("\\")[-1]

    # read in csv as pandas dataframe
    df = pd.read_csv(dataFileName)

    # if dataframe headers have spaces, replace with underscores
    df.columns = [col.replace(' ', '_').lower() for col in df.columns]

    # create table name by taking the file name and replacing spaces with underscore and dropping the file extention
    sqlite_table = dataFileName.replace('.csv', '').replace(' ', '_')

    # write dataframe to sqlite, overwrite table if it exists
    df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

# after the process completes, closes the databasse connection
sqlite_connection.close()

''' 

Code Breakdown
First, we’ll need to create a connection to a database — for that, we’ll use SQLAlchemy. Note the extension on the database name is .sqlite.

Next, assuming we are in the directory with the CSV file(s), we’ll get the path of the current working directory. Using glob, we’ll get a list of CSV file(s) in the directory. From there, we can iterate over that list.

For each file, split it based on the \(not included another \ because it was treating as a command  ) and take the last element (the actual filename) and create a pandas dataframe from the CSV.

The next two commands do a bit of clean up for the headers and table name (you may need to customize this part to suite your needs).

Finally, we write the dataframe to the SQLite database.

Basically, a new table is created for each CSV in the directory. 

'''