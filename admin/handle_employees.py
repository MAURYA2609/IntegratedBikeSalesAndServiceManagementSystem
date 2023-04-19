import curses

import admin.admin_options
import crud_options
import connector

stdscr = curses.initscr()
def start():
    operation = crud_options.get_selected_crud()
    if(operation == 0):
        add_employee()
    elif(operation == 1):
        read_employee()
    elif(operation == 2):
        update_employee()
    else :
        delete_employee()

def add_employee():
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        employeeID = input("Enter employee ID: ")
        name = input("Enter your Name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        designation = input("Enter designation: ")
        salary = input("Enter salary: ")
        joinDate = input("Enter joining date: ")
        showroomID = input("Enter showroom ID: ")

        cur.callproc('add_employee', (employeeID, name, email, phone, salary, designation, joinDate, showroomID))

        conn.commit()
        print("Employee added successfully!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()

def read_employee():
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        cur.callproc('select_all_employees')
        results = cur.fetchall()

        if len(results) == 0:
            print("No employees found.")
        else:
            print("{:<15} {:<15} {:<25} {:<25} {:<10} {:<40} {:<5} {:<10}".format("Employee ID", "Name", "Email", "Phone", "Salary", "Designation", "Joining Date", "Showroom ID"))
            for result in results:
                print("{:<15} {:<15} {:<25} {:<25} {:<10} {:<40} {:<5} {:<10}".format(result[0], result[1], result[3], result[2], result[4], result[5], result[6], result[7]))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()



def update_employee():
    conn = connector.connect_to_database()
    cur = conn.cursor()
    employeeID = input("Enter employee ID to update: ")
    name = input("Enter updated Name: ")
    email = input("Enter updated email: ")
    phone = input("Enter updated phone number: ")
    designation = input("Enter updated designation: ")
    salary = input("Enter updated salary: ")
    joinDate = input("Enter updated joining date: ")
    showroomID = input("Enter updated showroom ID: ")

    try:
        cur.callproc('update_employee', (employeeID, name, email, phone, salary, designation, joinDate, showroomID))
        # Check if any rows were affected by the update operation
        message = cur.fetchone()[0]
        print(message)
        conn.commit()
        print("Employee updated successfully!")
    except Exception as e:
        print(f"Error updating bike: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()


def delete_employee():
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        employee_id = input("Enter employee ID of the employee you want to delete: ")

        # Call the stored procedure
        # to delete the employee with the given employee ID
        cur.callproc('delete_employee', (employee_id,))

        # Check if any rows were affected by the delete operation
        result = cur.fetchone()
        if result[0] == 0:
            print(f"No employee with employee ID {employee_id} found.")
        else:
            print(f"Employee with ID {employee_id} deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.commit()
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()