import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE aplikasi_database")

print("Database berhasil dibuat!")