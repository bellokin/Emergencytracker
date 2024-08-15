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
  
# try:
#   cursor = connection.cursor()
#   cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, Email VARCHAR(255), Username VARCHAR(255), Password VARCHAR(255))")
  # cursor.execute("INSERT INTO Users (id, Email, Username, Password) VALUES (%s,%s,%s,%s)", ("001","Basseyimoh3012@gmail.com","Emore","ivbwe98v34o2"))
  # cursor.execute("SELECT * FROM Users")
  # cursor.execute("Show Tables")
#   print(cursor.fetchall())
# finally:
#   connection.close()

def authenticate(username, password):
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Users WHERE Username = %s and Password = %s", (username,password))
    result = cursor.fetchall()
    result = result[0]

    if result is not None:
      return result
    else:
      return None
    
  except Exception as error:
    print("An Error has occured: ", error)
  finally:
    connection.close()

# def register(Email, Username, Password):
#   try:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO Users (id, Email, Username, Password) VALUES (%s,%s,%s,%s)", ("001","Basseyimoh3012@gmail.com","Emore","ivbwe98v34o2"))
#   except Exception as error:
#     print("An Error has occured: ", error)
#   finally:
#     connection.close()

# WOrk on the login tommorow