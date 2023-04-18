import crud_options
import connector

def start():
    operation = crud_options.get_selected_crud()
    if(operation == 0):
        add_insurance_company()
    elif(operation == 1):
        read_insurance_company()
    elif(operation == 2):
        update_insurance_company()
    else :
        delete_insurance_company()

def add_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()
    
    taxationID = input("Enter taxation ID: ")
    companyName = input("Enter company name: ")
    companyAddress = input("Enter company address: ")
    companyEmail = input("Enter company email: ")
    companyWebsite = input("Enter company website: ")
    companyRating = input("Enter company rating: ")
    policyTypes = input("Enter policy types (comma-separated): ").split(",")
    
    cur.callproc('add_insurance_company', (taxationID, companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes))
    
    conn.commit()
    print("Insurance company added successfully!")
    conn.close()

def read_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.callproc('read_insurance_company')
    results = cur.fetchall()

    if len(results) == 0:
        print("No insurance companies found.")
    else:
        print("{:<15} {:<15} {:<45} {:<25} {:<25} {:<10} {:<25}".format("Taxation ID", "Company Name", "Company Address", "Company Email", "Company Website", "Rating", "Policy Types"))
        for result in results:
            print("{:<15} {:<15} {:<45} {:<25} {:<25} {:<10} {:<25}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))

    conn.close()


def update_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()
    
    taxationID = input("Enter taxation ID to update: ")
    companyName = input("Enter new company name: ")
    companyAddress = input("Enter new company address: ")
    companyEmail = input("Enter new company email: ")

def delete_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    taxation_id = input("Enter taxation ID of the company you want to delete: ")

    # Call the stored procedure to delete the company with the given taxation ID
    cur.callproc('delete_insurance_company', (taxation_id,))

    # Check if any rows were affected by the delete operation
    result = cur.fetchone()
    print(result)

    conn.commit()
    conn.close()
