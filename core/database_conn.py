import pymysql
from django.http import JsonResponse
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

timeout = 10

connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db= os.getenv('DATABASE_NAME'),
  host= os.getenv('DATABASE_HOST'),
  password= os.getenv('DATABASE_PASSWORD'),
  read_timeout=timeout,
  port= int(os.getenv('DATABASE_PORT', 23673)),
  user= os.getenv('DATABASE_USER'),
  write_timeout=timeout,
)
  
# try:
#   cursor = connection.cursor()

    # cursor.execute("""
    #                CREATE TABLE IF NOT EXISTS Users (
    #                 id INTEGER PRIMARY KEY AUTO_INCREMENT,
    #                 Email VARCHAR(255) UNIQUE,
    #                 Username VARCHAR(255) UNIQUE,
    #                 Password VARCHAR(255)
    #                 )
    #               """)
    # cursor.execute("SHOW TABLES")

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
    if result != ():
      return "User found"
    else:
      return "The User Doesn't exist"
    
  except Exception as error:
    return error
  finally:
    # connection.close()
    pass

def register(Email, Username, Password):
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = %s", (Username))
    result = cursor.fetchall()
    if result != ():
      return "Username already Exists!!"
    
    cursor.execute("SELECT * FROM Users WHERE Email = %s", (Email))
    result = cursor.fetchall()
    if result != ():
      return "Email already Exists!!"
    

    cursor.execute("INSERT INTO Users (Email, Username, Password) VALUES (%s,%s,%s)", (str(Email),str(Username),str(Password)))
    connection.commit()
    return "user added"
    
  except Exception as error:
    
    return error
  finally:
    # connection.close()
    pass
