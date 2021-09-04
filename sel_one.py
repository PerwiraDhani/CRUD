import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="aplikasi_database"
)

cursor = db.cursor()
sql = "SELECT * FROM people"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)