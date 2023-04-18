import connector


def start():
    read_bike()

def read_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.callproc('select_all_bikes')
    results = cur.fetchall()

    if len(results) == 0:
        print("No bikes found.")
    else:
        print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<50} {:<5} {:<5} {:<5}".format("Bike ID", "Bike Model Name", "Manufacturing Year", "Price", "Color", "Description", "Engine ID", "Showroom ID", "Policy Number"))
        for result in results:
            print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<50} {:<15} {:<15} {:<5}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    conn.close()