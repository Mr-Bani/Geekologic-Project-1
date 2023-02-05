import mysql.connector as db
import csv


db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "db_delino"


db_conn = db.connect(
  host=db_host,
  user=db_user,
  password=db_password
)

if db_conn :
    print("Connection to MYSQL successfully....")

cursor = db_conn.cursor()

cursor.execute("CREATE DATABASE {db_name}".format(db_name=db_name))


db_conn = db.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

cursor = db_conn.cursor()

cursor.execute("CREATE TABLE city(city_id INT AUTO_INCREMENT PRIMARY KEY,city_name VARCHAR(100))")
cursor.execute("CREATE TABLE restaurant_info(restaurant_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),delivery_duration VARCHAR(100),res_type VARCHAR(100))")
cursor.execute("CREATE TABLE address(address_id INT AUTO_INCREMENT PRIMARY KEY,city_id INT,restaurant_id INT,area VARCHAR(100),full_address TEXT,FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`),FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant_info` (`restaurant_id`))")
cursor.execute("CREATE TABLE rating(rating_id INT AUTO_INCREMENT PRIMARY KEY,restaurant_id INT,rate VARCHAR(100),rate_count VARCHAR(100),FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant_info` (`restaurant_id`))")
cursor.execute("CREATE TABLE menu(menu_id INT AUTO_INCREMENT PRIMARY KEY,restaurant_id INT, food_title VARCHAR(100),price VARCHAR(100),ingredient TEXT,FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant_info` (`restaurant_id`))")


csv_city_column =[]



sql_city = "INSERT INTO customers () VALUES (%s, %s)"
val_city = ("John", "Highway 21")
db.execute(sql_city, val_city)

sql_restaurant_info = "INSERT INTO customers () VALUES (%s, %s)"
val_restaurant_info = ("John", "Highway 21")
db.execute(sql_restaurant_info, val_restaurant_info)

sql_address = "INSERT INTO customers () VALUES (%s, %s)"
val_address = ("John", "Highway 21")
db.execute(sql_address, val_address)

sql_rating = "INSERT INTO customers () VALUES (%s, %s)"
val_rating = ("John", "Highway 21")
db.execute(sql_rating, val_rating)

db.commit()