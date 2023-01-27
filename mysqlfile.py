import mysql.connector


mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="getaway",
            password=""
        )

mycusor = mydb.cursor()
