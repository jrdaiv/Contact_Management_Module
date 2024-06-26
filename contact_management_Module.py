contact_book = {}
import re

def add_contacts(contact_book):
    print("Hello There...")
for i in range(1):
    first_name = input("Please Enter The First Name For This Contact. ")
    if not re.match(r"\w+", first_name):
        print("Is Not Valid. ")
    else:
        last_name = input("Please Enter The Last Name For This Contact. ")
        if not re.match(r"\w+", last_name):
            print("Is Not Valid. ")
        else:
            phone_num = input("Please Enter The Number For This Contact,\nWhile Following xxx-xxx-xxx Format. ")
            if not re.match(r"\d{3}-\d{3}-\d{4}", phone_num):
                print("Invalid. Please use xxx-xxx-xxxx format.\nContact Did Not Save Please Add Again. ")
            else:
                email = input("Please Enter The Email For This Contact,\nPlease Follow 'xxxx@xxx.com' Format. ")
                if not re.match(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
                    print("Invalid. Please use correct email format\nContact Did Not Save Please Add Again. ")
                else:
                    contact_book[first_name + " " + last_name] = {"First Name": first_name, "Last Name": last_name, "Phone": phone_num, "Email": email}
                    print(f"{contact_book} Has Been Successfully Added To The Directory. ")


def delete_contact(contact_book):
    remove_contact = input("Please Enter The Contact Name In Who You'd Like To Delete. ")
    if remove_contact in contact_book:
        del contact_book[remove_contact]
        print(f"{remove_contact} Has Now Been Deleted From The Directory. ")
    else:
        print("There Is Nobody Here By That Name. Please Try Again, Thank You. ")
    
def edit_contact(contact_book):
    contact_name = input("Please Enter The Full Contact Name You'd Like To Edit. ")
    if contact_name in contact_book:
        change_contacts = input("\nPlease Enter Numbers 1-4 On The Menu Below:\n1. Phone Number\n2. Email\n3. First Name\n4. Last Name\n")
        if change_contacts == "1":
            new_number = input("Please Enter The New Phone Number for This Person,\nWhile Following xxx-xxx-xxx Format. ")
            if not re.match(r"\d{3}-\d{3}-\d{4}", new_number):
                print("Invalid. Please use xxx-xxx-xxxx format.\nContact Did Not Save Please Try Again. ")
                return
            else:
                contact_book[contact_name]["Phone"] = new_number
                print(f"{contact_name} Number Has Now Been Changed To: {new_number} ")
        elif change_contacts == "2":
            new_email = input("Please Enter The New Email For This Person,\nPlease Follow 'xxxx@xxx.com' Format.? ")
            if not re.match(r"[A-Za-z0-9._%!$+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", new_email):
                print("Invalid. Please use correct email format.\nContact Did Not Save Please Try Again. ")
                return
            else:
                contact_book[contact_name]["Email"] = new_email
                print(f"{contact_name} Email Has Now Been Changed To: {new_email}.\n ")
        elif change_contacts == "3":
            new_first_name = input("Please Enter The New First Name You'd Like To Change For This Person? ")
            contact_book[contact_name]["First Name"] = new_first_name
            print(f"{contact_name} Has Now Been Changed To: {new_first_name}. ")
        elif change_contacts == "4":
            new_last_name = input("Please Enter The New Last Name You'd Like To Change For This Person?")
            contact_book[contact_name]["Last Name"] = new_last_name
            print(f"{contact_name} Has Now Been Changed To: {new_last_name}. ")
        else:
            print("Please Enter A Valid Response, Thank You. ")
    else:
        print("Eh Wrong Input. ")

def search_contact(contact_book): # NEED TO FIX THIS
    searched_contact = input("Please Enter The Contacts Full Name On Whom You Are Searching For. ")
    if searched_contact in contact_book:
        print(contact_book[searched_contact])
    else:
        print("Contact Not Found")


def display_contact(contact_book):
    for key in contact_book.keys():
        print(f"{contact_book[key]}")

def export_contact(contact_book):
    # pass
    try:
        with open("exported_contacts.txt", "w") as file:
            for i, info in contact_book.items():
                file.write(f"{i}: {info}\n")
                print(f"{contact_book}\nHas Been Officially Exported. ")
                print(f"{contact_book} Imported Successfully. ")

    except IOError:
        print(f"{contact_book} Ooof Looks Like Something Went Wrong. ")

def import_contact(filename):
    try:
        with open("exported_contact.txt", 'r') as file:
            
            for line in file:
                contact_id = line.strip().split()
                contact_book[line] = contact_id
        print(f"{filename} Imported Successfully.")
        return contact_book
    except FileNotFoundError:
        print(f"File not found: '{filename}'. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main(contact_book):
    while True:
        response = input("""   
                                                        Menu:
                            1. Add Contacts      4. Search Contacts    7. Import Contacts
                            2. Delete Contacts   5. Display Contacts   8. Quit
                            3. Edit Contacts     6. Export Contacts    
                            """)
        if response == "1":
            add_contacts(contact_book)
        elif response == "2":
            delete_contact(contact_book)
        elif response == "3":
            edit_contact(contact_book)
        elif response == "4":
            search_contact(contact_book)
        elif response == "5":
            display_contact(contact_book)
        elif response == "6":
            export_contact(contact_book)
        elif response == "7":
            import_contact(contact_book)
        elif response == "8":
            print("Ok, See Ya Next Time! ")
            break
        else:
            print("Please Input Proper Response, Thank You. ")

main(contact_book)
contacts = import_contact("exported_contacts.txt")
print(contacts)

