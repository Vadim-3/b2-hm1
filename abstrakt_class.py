from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_notes(self, notes):
        pass


#клас ConsoleInterface, реалізує інтерфейс користувача в консолі
class Interface(UserInterface):

    def show_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Address: {contact['address']}, E-Mail: {contact['e-mail']}, Birhday: {contact['birthday']}")

    def show_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(f"Title: {note['title']}, Content: {note['content']}")


# Список контактів і нотаток
contacts = [
    {"name": "Vadim", "phone": "123-456-7890", 'address': 'Mazepy 13', 'e-mail': 'newpost.67@gmail.com', 'birthday': '10.07.1989'},
    {"name": "Max", "phone": "987-654-3210", 'address': 'Franka 15b', 'e-mail': 'python@gmail.com', 'birthday': '09.08.2009'}
]

notes = [
    {"title": "tasks", "content": "1. draw a UML diagram 2. make an abstract class"},
    {"title": "affairs", "content": "buy food, pick up a package, go to grandma's"}
]

commands = {
    "add_contact": "Add a new contact.",
    "delete_contact": "Delete an existing contact.",
    "add_note": "Add a new note.",
    "delete_note": "Delete an existing note."
}

# Створила б'єкт консольного інтерфейсу
console_interface = Interface()

# Виведення контактів
console_interface.show_contacts(contacts)

# Виведення нотаток
console_interface.show_notes(notes)
