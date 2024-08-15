import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="EmergencyTracker",
  host="mysql-32342ae5-bellokingdavidibukun03-8a91.e.aivencloud.com",
  password="AVNS_X0YqYU2r7QUAL5TpN7Q",
  read_timeout=timeout,
  port=23673,
  user="avnadmin",
  write_timeout=timeout,
)
  
try:
  cursor = connection.cursor()
#   cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
#   cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
  cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
  print("Test")
finally:
  connection.close()