import hashlib
import time

import customer.customer_options
import login_options
import connector
from admin import admin_options
from customer import customer_options

def do_login():
    conn = connector.connect_to_database()
    username = input("Enter username : ")
    password = input("Enter password : ")
    encoded_password = hashlib.sha256(password.encode()).hexdigest()

    cur = conn.cursor()
    cur.callproc('authenticate_user', (username, encoded_password, ))

    result = cur.fetchone()
    if result is not None:
        if result[0] == "admin":
            print("Admin login successful!")
            admin_options.print_admin_options()
        elif result[0] == "customer":
            print("Customer Login successful!")
            customer_options.print_customer_options()
    else:
        print("Invalid credentials. Returning to main menu...")
        time.sleep(2)
        login_options.proceed_login()

    conn.close()

def do_signup():
    try:
        conn = connector.connect_to_database()
        username = input("Enter username : ")
        password = input("Enter password : ")
        encoded_password = hashlib.sha256(password.encode()).hexdigest()

        cur = conn.cursor()
        cur.callproc('signup_user', (username, encoded_password))
        print("Signed Up successfully!")
        conn.commit()
        customer.customer_options.print_customer_options()
    except Exception as e:
        print(f"Error: {e}")
        print("Returning to main menu...")
        time.sleep(2)
        login_options.proceed_login()
    finally:
        conn.close()
