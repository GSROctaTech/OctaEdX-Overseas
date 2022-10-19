import sqlite3
import os.path

class DBClass():
    path = os.path.dirname(os.path.abspath(__file__)) + '\CALENDER_APP.db'
    print(path)
    def __init__(self):

        print("\n\n\n %s \n\n\n", self.path)

        if not (os.path.isfile(self.path)):
            self.conn = sqlite3.connect('CALENDER_APP.db')
            print("\n DB schema created successfully")
            self.c = self.conn.cursor()
            self.createDBTables()
            self.createDBEntries()
            self.close()

    def createDBConnection(self):
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()

    def getDBpath(self):
        return self.path;

    def getCursor(self):
        return self.c;

    def getConnection(self):
        return self.conn;

    def close(self):
        try:
            self.c.close()
            self.conn.close()
        except sqlite3.ProgrammingError as e:
            print(e)

    def createDBTables(self):
        try:
            self.c.execute('''CREATE TABLE USER_DETAILS( 
                                        USER_ID INT PRIMARY KEY NOT NULL UNIQUE,
                                        FNAME TEXT,
                                        LNAME TEXT,
                                        EMAIL BLOB UNIQUE)''')
            self.c.execute('''CREATE TABLE LOGIN_DETAILS(
                                        USER_ID INT PRIMARY KEY ,
                                        USERNAME TEXT NOT NULL UNIQUE,
                                        PASSWORD BLOB NOT NULL UNIQUE,
                                        FOREIGN KEY(USER_ID) REFERENCES USER_DETAILS(USER_ID) )''')
            self.c.execute('''CREATE TABLE USER_GROUPS(
                                        GRP_ID INT PRIMARY KEY NOT NULL UNIQUE,
                                        GRP_NAME TEXT UNIQUE)''')
            self.c.execute('''CREATE TABLE REASON_CODES(
                                        CODE_TYPE VARCHAR(15) UNIQUE NOT NULL,
                                        CODE_VALUE VARCHAR(20) UNIQUE NOT NULL)''')
            self.c.execute('''CREATE TABLE USR_BELONGS_GRP(
                                            GRP_ID INT,
                                            USER_ID INT,
                                            FOREIGN KEY(GRP_ID) REFERENCES USER_GROUPS(GRP_ID),
                                            FOREIGN KEY(USER_ID) REFERENCES USER_DETAILS(USER_ID))''')
            self.c.execute('''CREATE TABLE USR_TRANSCATIONS(
                                            USER_ID INT,
                                            START_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                                            END_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
                                            REASON VARCHAR(20),
                                            FOREIGN KEY(REASON) REFERENCES REASON_CODES(CODE_VALUE),
                                            FOREIGN KEY(USER_ID) REFERENCES USER_DETAILS(USER_ID))''')
            self.conn.commit()
        except sqlite3.ProgrammingError as e:
            print(e)

        print("\n Created Tables successfully")

    def createDBEntries(self):
        print("Insert values to tables")
        try:
            self.c.execute('''INSERT INTO USER_DETAILS VALUES(1,"Anushree", "TP", "a...@in.ibm.com")''')
            self.c.execute('''INSERT INTO LOGIN_DETAILS VALUES(1,"anush", "password")''')
            self.c.execute('''INSERT INTO REASON_CODES VALUES("LEAVE", "Leave")''')
            self.c.execute(
                '''INSERT INTO USR_TRANSCATIONS VALUES(1,'2017-07-09 10:00:00','2017-07-09 10:00:00',"Leave")''')
            self.c.execute('''INSERT INTO REASON_CODES VALUES("VACATION", "Vacation")''')
            self.conn.commit()

        except sqlite3.ProgrammingError as e:
            print(e)

        print("All Values inserted")
        print("Values inserted are:")

        try:
            print("USER DETAILS\n\n")
            for row in self.c.execute('SELECT * FROM USER_DETAILS'):
                print(row)

            print("LOGIN_DETAILS\n\n")
            for row in self.c.execute('SELECT * FROM LOGIN_DETAILS'):
                print(row)

            print("REASON_CODES\n\n")
            for row in self.c.execute('SELECT * FROM REASON_CODES'):
                print(row)

            print("USR_TRANSCATIONS\n\n")
            for row in self.c.execute('SELECT * FROM USR_TRANSCATIONS'):
                print(row)

        except sqlite3.ProgrammingError as e:
            print(e)

     self.db.createDBConnection()
     self.db.getCursor().execute('SELECT * FROM USR_TRANSCATIONS')
     all_rows = self.db.getCursor().fetchone()
     for row in all_rows:
         print(row)
     # row1=list(all_rows)
     self.db.close()
