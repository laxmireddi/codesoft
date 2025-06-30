 # Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        print("Leave field empty to keep current value.")
        phone = input(f"New phone (current: {contacts[name]['phone']}): ").strip()
        email = input(f"New email (current: {contacts[name]['email']}): ").strip()
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()