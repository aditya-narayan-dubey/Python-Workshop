
# Contact Book

contactlist = []

def addcontact():
    name = input("Enter name: ")
    address = input("Enter address: ")
    email_id = input("Enter email id: ")
    mobile = input("Enter mobile number: ")

    data = {
        "name": name,
        "address": address,
        "email_id": email_id,
        "mobile": mobile
    }

    contactlist.append(data)
    print("Contact added successfully!")


def display():
    if len(contactlist) == 0:
        print("Record is not found")

    else:
        print("=== Contact List ===")

        for x in contactlist:
            print("Name:", x["name"])
            print("Address:", x["address"])
            print("Email ID:", x["email_id"])
            print("Mobile:", x["mobile"])
            print("=========================")


while True:
    print("\n1 for add contact")
    print("2 for display contact")
    print("0 for exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        addcontact()

    elif ch == 2:
        display()

    elif ch == 0:
        print("Contact Book Exited")
        break

    else:
        print("Invalid Choice")
