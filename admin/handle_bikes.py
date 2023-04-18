import crud_options
import connector

def start():
    operation = crud_options.get_selected_crud()
    if operation == 0:
        add_bike()
    elif operation == 1:
        read_bike()
    elif operation == 2:
        update_bike()
    else:
        delete_bike()

def add_bike():
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

    cur.execute("""INSERT INTO Bike
                (bikeID, bikeModelName, bikeManufacturingYear, bikePrice, bikeColor, bikeDescription, engineID, showroomID, policyNumber)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (bike_id, bike_model_name, bike_manufacturing_year, bike_price, bike_color, bike_description, engine_id, showroom_id, policy_number))

    conn.commit()
    print("Bike added successfully!")
    conn.close()

def read_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Bike")
    results = cur.fetchall()

    if len(results) == 0:
        print("No bikes found.")
    else:
        print("{:<10} {:<30} {:<20} {:<10} {:<15} {:<25} {:<10} {:<10} {:<15}".format("Bike ID", "Bike Model Name", "Manufacturing Year", "Price", "Color", "Description", "Engine ID", "Showroom ID", "Policy Number"))
        for result in results:
            print("{:<10} {:<30} {:<20} {:<10} {:<15} {:<25} {:<10} {:<10} {:<15}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    conn.close()

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

    cur.execute("""UPDATE Bike SET bikeModelName = %s, bikeManufacturingYear = %s, bikePrice = %s, bikeColor = %s,
                bikeDescription = %s, engineID = %s, showroomID = %s, policyNumber = %s WHERE bikeID = %s""",
                (bike_model_name, bike_manufacturing_year, bike_price, bike_color, bike_description, engine_id, showroom_id, policy_number, bike_id))

    conn.commit()
    print("Bike updated successfully!")
    conn.close()


def delete_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    bike_id = input("Enter ID of the bike you want to delete: ")

    # Call the stored procedure to delete the bike with the given ID
    cur.callproc('delete_bike', (bike_id,))

    # Check if any rows were affected by the delete operation
    result = cur.fetchone()
    if result[0] == 0:
        print(result)
    else:
        print(f"Bike with ID {bike_id} deleted successfully.")

    conn.commit()
    conn.close()