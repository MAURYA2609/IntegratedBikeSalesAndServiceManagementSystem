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
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        department = input("Enter department: ")
        salary = input("Enter salary: ")

        cur.execute("""INSERT INTO Employees
                    (employeeID, firstName, lastName, email, phone, address, department, salary)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (employeeID, firstName, lastName, email, phone, address, department, salary))

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

        cur.execute("SELECT * FROM Employees")
        results = cur.fetchall()

        if len(results) == 0:
            print("No employees found.")
        else:
            print("{:<15} {:<15} {:<15} {:<25} {:<10} {:<40} {:<5} {:<10}".format("Employee ID", "First Name", "Last Name", "Email", "Phone", "Address", "Department", "Salary"))
            for result in results:
                print("{:<15} {:<15} {:<15} {:<25} {:<10} {:<40} {:<5} {:<10}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
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
    conn = None
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        employeeID = input("Enter employee ID to update: ")
        firstName = input("Enter new first name: ")
        lastName = input("Enter new last name: ")
        email = input("Enter new email: ")
        phone = input("Enter new phone number: ")
        address = input("Enter new address: ")
        department = input("Enter new department: ")
        salary = input("Enter new salary: ")

        cur.execute("""UPDATE Employees SET firstName = %s, lastName = %s, email = %s, phone = %s,
                    address = %s, department = %s, salary = %s WHERE employeeID = %s""",
                    (firstName, lastName, email, phone, address, department, salary, employeeID))

        conn.commit()
        print("Employee updated successfully!")
    except connector.errors.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
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

        # Call the stored procedure to delete the employee with the given employee ID
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