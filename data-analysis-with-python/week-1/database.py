from decouple import config
import pymysql.cursors

# Accessing Databases with Python
print(config('DB_HOST') + config('USER') + config('DB_PASSWORD') + config('DB'))
connection = pymysql.connect(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password="",
    db=config('DB'),
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO users (email, password) VALUES (%s, %s);'
        cursor.execute(sql, ('testguy@gmail.com', 'secret'))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchone()
finally:
    connection.close()
print(config('PASSWORD'))
