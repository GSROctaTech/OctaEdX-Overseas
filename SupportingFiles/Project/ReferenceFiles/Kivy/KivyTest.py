# main.py
import sqlite3
import os.path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class DBClass():

    def __init__(self):

        self.conn = sqlite3.connect('DUMMY_SCHEMA.db')
        print("\n DB schema created successfully")
        self.c = self.conn.cursor()
        self.createDBSchema(self)

        # created db already and trying to connect to the db file created.
        # self.db_path = "./DUMMY_SCHEMA.db"
        # self.conn= sqlite3.connect(self.db_path)
        # self.c=self.conn.cursor()

    def getDBpath(self):
        return self.db_path;

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

    def createDBSchema(self):
        self.c.execute('''CREATE TABLE DUMMY( 
                                        FNAME TEXT,
                                        LNAME TEXT)''')

        print("\n Created Tables successfully")
        self.conn.commit()
        print("\n DB commands Commited")

        print("Insert values to tables")
        self.c.execute('''INSERT INTO DUMMY VALUES("Ramesh","C")''')
        self.c.execute('''INSERT INTO DUMMY VALUES("Saya","S")''')
        self.c.execute('''INSERT INTO DUMMY VALUES("CHANDRAN","N")''')
        print("Values inserted")
        self.conn.commit()


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")


class MainApp(App):
    db = DBClass()

    def build(self):
        return presentation

    def printdb(self):
        self.db.getCursor().execute('SELECT * FROM DUMMY')
        all_rows = self.db.getCursor().fetchall()
        for row in all_rows:
            print(row)

        self.db.close()


MainApp().run()
