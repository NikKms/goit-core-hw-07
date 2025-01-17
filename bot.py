from colorama import Fore

import birthday
from address_book import AddressBook
from decorators.input_error import input_error
from record import Record


class Bot:
    def __init__(self):
        self.book = AddressBook()

    @input_error
    def __parse_input(self, inpt):
        parts = inpt.split()
        if not parts:
            return "", []
        cmd = parts[0].strip().lower()
        args = parts[1:]
        return cmd, args

    def __find_record_or_error(self, name):
        record = self.book.find(name)
        if not record:
            raise ValueError(f"{Fore.RED}Contact '{name}' not found.")
        return record

    def __check_empty_book(self):
        if not self.book:
            return f"{Fore.YELLOW}Your phonebook is empty 😒"
        return None

    def __find_record(self, name):
        record = self.book.find(name)
        if not record:
            return None, f"{Fore.RED}Contact '{name}' not found."
        return record, None

    @staticmethod
    def __format_contact_phones(record):
        return "; ".join([f"{Fore.GREEN}{phone.value}" for phone in record.phones])

    @input_error
    def __add_contact(self, args):
        name, phone = args
        record, _ = self.__find_record(name)

        if not record:
            record = Record(name)
            self.book.add_record(record)
            message = f"{Fore.GREEN}Contact {name} added."
        else:
            message = f"{Fore.GREEN}Contact {name} updated."

        record.add_phone(phone)
        return message

    @input_error
    def __change_contact(self, args):
        empty_message = self.__check_empty_book()
        if empty_message:
            return empty_message

        name, old_phone, new_phone = args
        record, error_message = self.__find_record(name)
        if error_message:
            return error_message

        try:
            record.edit_phone(old_phone, new_phone)
            return f"{Fore.GREEN}Contact '{name}' updated successfully."
        except ValueError as e:
            return f"{Fore.RED}Error: {e}"

    @input_error
    def __show_phone(self, args):
        empty_message = self.__check_empty_book()
        if empty_message:
            return empty_message

        name = args[0]
        record, error_message = self.__find_record(name)
        if error_message:
            return error_message

        phones = self.__format_contact_phones(record)
        return f"📔 {Fore.CYAN}{name} : 📞 {phones}"

    @input_error
    def __show_all(self):
        empty_message = self.__check_empty_book()
        if empty_message:
            return empty_message

        res = []
        for name, record in self.book.items():
            phones = "; ".join(phone.value for phone in record.phones)
            b_day = f"🥳 {Fore.YELLOW}{record.birthday.value}" if record.birthday else f"{Fore.RED}No birthday set"
            res.append(f"📔 {Fore.CYAN}{name} : 📞 {Fore.GREEN}{phones} | {b_day}")

        return "\n".join(res)

    @input_error
    def __add_birthday(self, args):
        name, birthday = args
        record = self.__find_record_or_error(name)
        record.add_birthday(birthday)
        return f"{Fore.GREEN}Birthday added for {name}."

    @input_error
    def __show_birthday(self, args):
        name = args[0]
        record = self.__find_record_or_error(name)
        return record.show_birthday()

    @input_error
    def __birthdays(self):
        upcoming_birthdays = self.book.get_upcoming_birthdays()
        if not upcoming_birthdays:
            return f"{Fore.YELLOW}No upcoming birthdays found."

        res = [
            f"🎉 {Fore.CYAN}{entry['name']}: {Fore.GREEN}{entry['birthday']}"
            for entry in upcoming_birthdays
        ]
        return "\n".join(res)

    @staticmethod
    def show_help():
        return f"""{Fore.BLUE}Available commands:
       {Fore.CYAN}hello - greet the bot
       {Fore.CYAN}add [name] [phone] - add a new contact
       {Fore.CYAN}change [name] [old phone] [new phone] - change a phone number
       {Fore.CYAN}phone [name] - show the phone number of a contact
       {Fore.CYAN}all - show all contacts
       {Fore.CYAN}add-birthday [name] [birthday] - add a birthday
       {Fore.CYAN}show-birthday [name] [birthday] - add a birthday
       {Fore.CYAN}birthdays - show upcoming birthdays
       {Fore.CYAN}help - show available commands
       {Fore.CYAN}close/exit - exit the bot
       """

    def start_bot(self):
        print(
            f"{Fore.MAGENTA}Welcome to the assistant bot! \n"
            f"{Fore.YELLOW}Type 'help' to see available commands or 'hello' to get started."
        )

        while True:
            user_input = input(f"{Fore.CYAN}Enter a command: ").strip()
            if not user_input:
                print(f"{Fore.RED}Invalid command. Type 'help' to see available commands.")
                continue

            try:
                command, args = self.__parse_input(user_input)
            except ValueError as e:
                print(f"{Fore.RED}Error: {e}")
                continue

            if command in ["close", "exit"]:
                print(f"{Fore.MAGENTA}Good bye!")
                break
            elif command == "hello":
                print(f"{Fore.MAGENTA}How can I help you?")
            elif command == "add":
                print(self.__add_contact(args))
            elif command == "change":
                print(self.__change_contact(args))
            elif command == "phone":
                print(self.__show_phone(args))
            elif command == "all":
                print(self.__show_all())
            elif command == "add-birthday":
                print(self.__add_birthday(args))
            elif command == "show-birthday":
                print(self.__show_birthday(args))
            elif command == "birthdays":
                print(self.__birthdays())
            elif command == "help":
                print(self.show_help())
            else:
                print(f"{Fore.RED}Invalid command. Type 'help' to see available commands.")
