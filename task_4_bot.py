from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name]
    contacts[name] = phone
    return "Contact updated"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args, contacts):
    if not contacts:
         return "Empty contacts"
     
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    else:
        command = parts[0].lower()
        args = parts[1:]
    return command, args
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command in commands:
            print(commands[command](args, contacts))

        else:
            print("Invalid command.")
            
if __name__ == "__main__":
    main()