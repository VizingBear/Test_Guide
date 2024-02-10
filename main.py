import json


def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

    return contacts


def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)


def display_contacts(page_num, page_size, contacts):
    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size
    for contact in contacts[start_idx:end_idx]:
        print(contact)


def add_contact(contacts, contact):
    contacts.append(contact)
    save_contacts(contacts)


def edit_contact(contacts, index, new_contact):
    contacts[index] = new_contact
    save_contacts(contacts)


def search_contacts(contacts, **kwargs):
    result = []
    for contact in contacts:
        if all(item in contact.items() for item in kwargs.items()):
            result.append(contact)
    return result


def main():
    contacts = load_contacts()

    while True:
        print("\n1. Display contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Search contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            page_num = int(input("Enter page number: "))
            page_size = 5
            display_contacts(page_num, page_size, contacts)
        elif choice == "2":
            contact = {
                "last_name": input("Last Name: "),
                "first_name": input("First Name: "),
                "middle_name": input("Middle Name: "),
                "organization": input("Organization: "),
                "work_phone": input("Work Phone: "),
                "personal_phone": input("Personal Phone: ")
            }
            add_contact(contacts, contact)
        elif choice == "3":
            index = int(input("Enter index of contact to edit: "))
            new_contact = {
                "last_name": input("Last Name: "),
                "first_name": input("First Name: "),
                "middle_name": input("Middle Name: "),
                "organization": input("Organization: "),
                "work_phone": input("Work Phone: "),
                "personal_phone": input("Personal Phone: ")
            }
            edit_contact(contacts, index, new_contact)
        elif choice == "4":
            search_criteria = {}
            search_criteria["last_name"] = input("Last Name (Optional): ").strip()
            search_criteria["first_name"] = input("First Name (Optional): ").strip()
            search_criteria["organization"] = input("Organization (Optional): ").strip()
            search_result = search_contacts(contacts, **search_criteria)
            print("Search Results:")
            for contact in search_result:
                print(contact)
        elif choice == "5":
            save_contacts(contacts)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()