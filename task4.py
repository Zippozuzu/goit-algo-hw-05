def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"

    return inner

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number of {name} is {contacts[name]}"
    else:
        return "Name not found"
    

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found"
    
def man():
    content = '''
    Доступні команди:
    - "hello" -> 
        Введення: "hello"
        Вивід: "How can I help you?"
    - "add [ім'я] [номер телефону]" -> 
        Приклад введення: "add John 1234567890"
        Вивід: "Contact added."
    - "change [ім'я] [новий номер телефону]" -> 
        Приклад введення: "change John 0987654321"
        Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
    - "phone [ім'я]" -> 
        Приклад введення: "phone John"
        Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
    - "all" -> 
        Введення: "all"
        Вивід: усі збережені контакти з номерами телефонів
    - "export" ->
        Введення: "export"
        Вивід: Буде створений "contacts.txt" з іменами і номерами телефонів
    - "close" або "exit"
        Введення: ""close" або "exit"
        Вивід: У консоль повідомлення "Good bye!". Бот завершує свою роботу
    '''
    print(content)

def show_all(contacts):
    if len(contacts) == 0:
        return "The contacts list is empty"
    else:
        for key, value in contacts.items():
            return f"{key}: {value}"


def export(contacts):
    if len(contacts) == 0:
        return "The contacts list is empty"
    else:
        with open("contacts.txt", 'w') as f:  
            for key, value in contacts.items():  
                f.write('%s -> %s\n' % (key, value))
        return "The contact list was created in ./contacts.txt"
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "man":
            man()
        elif command == "export":
            export(contacts)
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
                print(add_contact(args, contacts))
        elif command == "change":
                print(change_username_phone(args,contacts))
        elif command == "phone":
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Read the manual -> 'man' command")

if __name__ == "__main__":
    main()
