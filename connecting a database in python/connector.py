import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234",database="harsh")

mycursor=mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
	print(i)
