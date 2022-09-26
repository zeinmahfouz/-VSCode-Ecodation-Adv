import mysql.connector
connection = mysql.connector.connect(
  host="localhost",  #burada IP yazarak harici DB e bağlanabiliriz
    user="root",
    password="1998"
)
print(connection)


if connection.is_connected():
  print("bağlandı")
else:
    print("bağlantı hatası")
