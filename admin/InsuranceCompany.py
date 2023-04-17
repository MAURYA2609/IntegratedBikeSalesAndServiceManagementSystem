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
    
    cur.execute("""INSERT INTO InsuranceCompany
                (taxationID, companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (taxationID, companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes))
    
    conn.commit()
    print("Insurance company added successfully!")
    conn.close()

def read_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM InsuranceCompany")
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
    companyWebsite = input("Enter new company website: ")
    companyRating = input("Enter new company rating: ")
    policyTypes = input("Enter new policy types (comma-separated): ").split(",")
    
    cur.execute("""UPDATE InsuranceCompany SET companyName = %s, companyAddress = %s, companyEmail = %s, companyWebsite = %s,
                companyRating = %s, policyTypes = %s WHERE taxationID = %s""",
                (companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes, taxationID))
    
    conn.commit()
    print("Insurance company updated successfully!")
    conn.close()

def delete_insurance_company():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    taxation_id = input("Enter taxation ID of the company you want to delete: ")

    # Call the stored procedure to delete the company with the given taxation ID
    cur.callproc('delete_insurance_company', (taxation_id,))

    # Check if any rows were affected by the delete operation
    result = cur.fetchone()
    if result[0] == 0:
        print(f"No company with taxation ID {taxation_id} found.")
    else:
        print(f"Company with taxation ID {taxation_id} deleted successfully.")

    conn.commit()
    conn.close()
