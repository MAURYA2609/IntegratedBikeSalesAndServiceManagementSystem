import hashlib
import login_options
import connector
from admin import admin_options


def do_login():
    conn = connector.connect_to_database()
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.callproc('authenticate_user', (username, encoded_password, ))

    result = cur.fetchone()[0]

    if result is not None:
        if result == "admin":
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
    cur.callproc('signup_user', (username, encoded_password))

    conn.commit()
    conn.close()
