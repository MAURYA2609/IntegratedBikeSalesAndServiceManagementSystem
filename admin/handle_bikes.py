import curses
import admin.admin_options
import crud_options
import connector

stdscr = curses.initscr()
def start():
    try:
        operation = crud_options.get_selected_crud()
        if operation == 0:
            add_bike()
        elif operation == 1:
            read_bike()
        elif operation == 2:
            update_bike()
        else:
            delete_bike()
    except Exception as e:
        print(f"Error: {e}")

def add_bike():
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        bike_id = input("Enter bike ID: ")
        bike_model_name = input("Enter bike model name: ")
        bike_manufacturing_year = input("Enter bike manufacturing year: ")
        bike_price = input("Enter bike price: ")
        bike_color = input("Enter bike color: ")
        bike_description = input("Enter bike description: ")
        engine_id = input("Enter engine ID: ")
        showroom_id = input("Enter showroom ID: ")
        policy_number = input("Enter policy number: ")

        # Call the stored procedure to add the bike
        cur.callproc('add_bike', (
        bike_id, bike_model_name, bike_manufacturing_year, bike_price, bike_color, bike_description, engine_id,
        showroom_id, policy_number))

        conn.commit()
        print("Bike added successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()


def read_bike():
    try:
        conn = connector.connect_to_database()
        cur = conn.cursor()

        cur.callproc('select_all_bikes')
        results = cur.fetchall()

        if len(results) == 0:
            print("No bikes found.")
        else:
            print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<50} {:<5} {:<5} {:<5}".format("Bike ID", "Bike Model Name",
                                                                                       "Manufacturing Year", "Price",
                                                                                       "Color", "Description",
                                                                                       "Engine ID", "Showroom ID",
                                                                                       "Policy Number"))
            for result in results:
                print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<50} {:<5} {:<5} {:<5}".format(result[0], result[2],
                                                                                           result[3], result[4],
                                                                                           result[5], result[6],
                                                                                           result[7], result[8],
                                                                                           result[9]))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()


def update_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    bike_id = input("Enter bike ID to update: ")
    bike_model_name = input("Enter new bike model name: ")
    bike_manufacturing_year = input("Enter new bike manufacturing year: ")
    bike_price = input("Enter new bike price: ")
    bike_color = input("Enter new bike color: ")
    bike_description = input("Enter new bike description: ")
    engine_id = input("Enter new engine ID: ")
    showroom_id = input("Enter new showroom ID: ")
    policy_number = input("Enter new policy number: ")

    try:
        cur.callproc('update_bike', (bike_id, bike_model_name, bike_manufacturing_year, bike_price, bike_color, bike_description, engine_id, showroom_id, policy_number))
        # Check if any rows were affected by the update operation
        conn.commit()
        print("Updated Successfully!!")
    except Exception as e:
        print(f"Error updating bike: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()


def delete_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    bike_id = input("Enter ID of the bike you want to delete: ")

    try:
        # Call the stored procedure to delete the bike with the given ID
        cur.callproc('delete_bike', (bike_id,))
        # Check if any rows were affected by the delete operation
        message = cur.fetchone()[0]
        print(message)
        conn.commit()
    except Exception as e:
        print(f"Error deleting bike: {e}")
        conn.rollback()
    finally:
        conn.close()
        print("Press Enter to return to Main Menu...")
        key = stdscr.getch()
        if key == ord("\n"):
            admin.admin_options.print_admin_options()
