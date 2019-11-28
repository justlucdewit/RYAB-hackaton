import mysql.connector

def connectWithDataBase(host, username, passwd):
    db = mysql.connector.connect(host=host, user=username, passwd=passwd)
    return db, db.cursor()

def showDatabaseList(cursor):
    databases = []
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        databases.append(x[0])
    return databases
    