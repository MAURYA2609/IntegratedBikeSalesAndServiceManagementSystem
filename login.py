import hashlib
import options
import connector


def do_login():
    conn = connector.connect_to_database()
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = %s", (username, encoded_password))

    result = cur.fetchone()
    count = result[0]
    if count == 1:
        print("Login successful!")
    else:
        print("Invalid credentials. Please try again.")
        options.proceed_login()

    conn.close()


def do_signup():
    conn = connector.connect_to_database()
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, encoded_password))

    conn.commit()
    conn.close()

