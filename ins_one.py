import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="aplikasi_database"
)


cursor = db.cursor()
sql = "INSERT INTO people (name, address) VALUES (%s, %s)"
val = ("Perwira", "Madiun")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))