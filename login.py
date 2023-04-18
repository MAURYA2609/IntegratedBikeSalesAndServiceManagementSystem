import hashlib
import login_options
import connector
from admin import admin_options


def do_login():
    admin_options.print_admin_options()
    conn = connector.connect_to_database()
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = %s", (username, encoded_password))

    result = cur.fetchone()
    count = result[0]
    if count == 1:
        cur.execute("SELECT user_type FROM users WHERE username = %s AND password = %s", (username, encoded_password))
        user_type = cur.fetchone()[0]
        if user_type == "admin":
            print("Admin login successful!")
            admin_options.print_admin_options()
        else:
            print("Login successful!")
            user_options.print_user_options()
    else:
        print("Invalid credentials. Please try again.")
        login_options.proceed_login()

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
