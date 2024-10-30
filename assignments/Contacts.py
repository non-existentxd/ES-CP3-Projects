
#polymorphism for this assignment
class Contacts:
    def __init__(self):
        self.view = 'quit'
        self.contact_list = []
        self.choice = None
        self.index = None

    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            for index, contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
        self.handle_choice()

    def handle_choice(self):
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'
        elif self.choice.isnumeric() and self.view == 'list':
            index = int(self.choice) - 1
            if 0 <= index < len(self.contact_list):
                self.index = index
                self.view = 'info'

    def show_info(self):
        self.contact_list[self.index].display_info()
        self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
        self.handle_info_choice()

    def handle_info_choice(self):
        if self.choice == 'c':
            self.view = 'list'
        elif self.choice == 'n':
            self.index = (self.index + 1) % len(self.contact_list)
        elif self.choice == 'p':
            self.index = (self.index - 1) % len(self.contact_list)
        elif self.choice == 'q':
            self.view = 'quit'

    def add_contact(self):
        new_contact = Information()
        self.contact_list.append(new_contact)
        self.view = 'list'

    def display(self):
        self.view = 'list'
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'info':
                self.show_info()
            elif self.view == 'add':
                self.add_contact()
            elif self.view == 'quit':
                print('\nClosing the contact list...\n')
                break

class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')

    def display_info(self):
        print(f'\n{self.first_name} {self.last_name}')
        print(f'Personal phone number: {self.personal_phone}')
        print(f'Personal email address: {self.personal_email}')
        print(f'Work title: {self.title}')
        print(f'Work phone number: {self.work_phone}')
        print(f'Work email address: {self.work_email}')


contacts = Contacts()
contacts.display()
