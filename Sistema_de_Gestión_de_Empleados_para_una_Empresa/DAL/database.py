import mysql.connector

db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "ddl"  

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

mycursor = mydb.cursor()