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
    cur.callproc('authenticate_user', [username, encoded_password, '@p_user_type'])

    result = cur.fetchone()
    if result is not None:
        user_type = result[0]
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
    cur.callproc('signup_user', (username, encoded_password))

    conn.commit()
    conn.close()
