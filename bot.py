def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Error: Key '{e.args[0]}' does not exist."
        except IndexError:
            return "Error: Insufficient arguments."

    return inner

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command format for adding a contact."

@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Phone number updated for {name}."
        else:
            return f"{name} does not exist in contacts."
    else:
        return "Invalid command format for changing a contact's phone number."

@input_error
def get_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"Phone number for {name}: {contacts[name]}"
        else:
            return f"{name} does not exist in contacts."
    else:
        return "Invalid command format for retrieving a phone number."

@input_error
def display_all(contacts):
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(display_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
