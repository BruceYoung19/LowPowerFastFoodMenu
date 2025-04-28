import sqlite3

def connectDatabase():
   with sqlite3.connect("foodshop.db") as connection:
        
       cusor = connection.cursor():
       print ("Connected To The Database Successfully")
       
       # Making each of the database

       create_menu_table = '''
       CREATE TABLE IF NOT EXISTS menu(
       menuid INTERGER PRIMARY KEY AUTOCREMENT,
       menuitemname TEXT NOT NULL,
       description TEXT NOT NULL,
       price INTERGER,
       );
       '''

       create_user_table= '''
       CREATE TABLE IF NOT EXISTS user(
       userid INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT NOT NULL,
       favouriteOrder INTEGER,
        );
       '''
       
       create_order_table'''
       CREATE TABLE IF NOT EXISTS order(
       orderid PRIMARY KEY AUTOINCREMENT,
       menuid TEXT NOT NULL,
       );
       '''
       
       cusor.execute(create_menu_table)
       cusor.execute(create_user_table)
       cusor.execute(create_order_table)
       
       connection.commit()

def creatingusers():
     with sqlite3.connect("foodshop.db") as connection:
        cusor = connection.cursor();

def readDatabases():
      with sqlite3.connect("foodshop.db") as connection:
        cusor = connection.cursor();
    
   
connectDatabase()
