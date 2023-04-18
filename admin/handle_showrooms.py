import crud_options
import connector

def start():
    operation = crud_options.get_selected_crud()
    if operation == 0:
        add_showroom()
    elif operation == 1:
        read_showroom()
    elif operation == 2:
        update_showroom()
    else:
        delete_showroom()

def add_showroom():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    showroom_id = input("Enter showroom ID: ")
    showroom_name = input("Enter showroom name: ")
    showroom_address = input("Enter showroom address: ")
    showroom_email = input("Enter showroom email: ")
    showroom_phone = input("Enter showroom phone: ")

    cur.execute("""INSERT INTO Showroom
                (showroomID, showroomName, showroomAddress, showroomEmail, showroomPhone)
                VALUES (%s, %s, %s, %s, %s)""",
                (showroom_id, showroom_name, showroom_address, showroom_email, showroom_phone))

    conn.commit()
    print("Showroom added successfully!")
    conn.close()

def read_showroom():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Showroom")
    results = cur.fetchall()

    if len(results) == 0:
        print("No showrooms found.")
    else:
        print("{:<15} {:<25} {:<45} {:<25} {:<15}".format("Showroom ID", "Showroom Name", "Showroom Address", "Showroom Email", "Showroom Phone"))
        for result in results:
            print("{:<15} {:<25} {:<45} {:<25} {:<15}".format(result[0], result[1], result[2], result[3], result[4]))

    conn.close()

def update_showroom():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    showroom_id = input("Enter showroom ID to update: ")
    showroom_name = input("Enter new showroom name: ")
    showroom_address = input("Enter new showroom address: ")
    showroom_email = input("Enter new showroom email: ")
    showroom_phone = input("Enter new showroom phone: ")

    cur.execute("""UPDATE Showroom SET showroomName = %s, showroomAddress = %s, showroomEmail = %s, showroomPhone = %s
                WHERE showroomID = %s""",
                (showroom_name, showroom_address, showroom_email, showroom_phone, showroom_id))

    conn.commit()
    print("Showroom updated successfully!")
    conn.close()

def delete_showroom():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    showroom_id = input("Enter ID of the showroom you want to delete: ")

    # Call the stored procedure to delete the showroom with the given ID
    cur.callproc('delete_showroom', (showroom_id,))

    # Check if any rows were affected by the delete operation
    result = cur.fetchone()
    if result[0] == 0:
        print(f"No showroom with ID {showroom_id} found.")
    else:
        print(f"Showroom with ID {showroom_id} deleted successfully.")

    conn.commit()
    conn.close()

