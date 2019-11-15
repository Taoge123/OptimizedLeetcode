import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="52775277",
    database="testdb"
)

mycuror = mydb.cursor()

# mycuror.execute("CREATE DATABASE testdb")
mycuror.execute("SHOW DATABASES")
# for db in mycuror:
    # print(db)

# mycuror.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# mycuror.execute("SHOW DATABASES")
# for tb in mycuror:
#     print(tb)


