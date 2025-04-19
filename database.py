import sqlite3

def connectDatabase():
   with sqlite3.connect("foodshop.db") as connection:
        
       cusor = connection.cursor():
       print ("Connected To The Database Successfully")
       
       # Making each of the database

       create_menu_table = '''
       '''

       create_user_table= '''
       '''
       
       create_order_table'''
       '''
       
       cusor.execute(create_menu_table)
       cusor.execute(create_user_table)
       cusor.execute(create_order_table)
       
       connection.commit()

def creatingusers():
     with sqlite3.connect("foodshop.db") as connection:
        cusor = connection.cursor();


connectDatabase()
