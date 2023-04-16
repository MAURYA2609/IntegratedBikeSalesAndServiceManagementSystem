import pymysql
import hashlib


def connect_to_database():
    # Connect to MySQL database
    try:
        conn = pymysql.connect(
            host="localhost",
            password="payruam",
            user="root",
            database="ibssms"
        )
        proceed_login(conn)
    except pymysql.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))


def proceed_login(conn):
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, encoded_password))

    conn.commit()
