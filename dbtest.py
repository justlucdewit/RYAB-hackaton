from helper import *

db, cursor = connectWithDataBase("localhost", "root", "password")

databases = showDatabaseList(cursor)

print(databases)