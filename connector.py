import pymysql


def connect_to_database():
    # Connect to MySQL database
    try:
        conn = pymysql.connect(
            host="localhost",
            password="MyNewPass",
            user="root",
            database="ibssms"
        )
        return conn
    except pymysql.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
