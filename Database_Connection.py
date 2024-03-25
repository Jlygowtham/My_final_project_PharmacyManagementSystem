import mysql.connector

def connection():
    try:
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="pharamacy")
        mycursor=mysqldb.cursor()
        return mycursor, mysqldb
    
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()