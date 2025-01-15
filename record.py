from birthday import Birthday
from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __get_phone_or_raise(self, phone: str)->Phone:
        phone_obj = self.find_phone(phone)
        if phone_obj is None:
            raise ValueError(f"Phone number {phone} not found")
        return phone_obj

    def add_phone(self, phone:str)-> None:
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone:str)-> None:
        phone_obj = self.__get_phone_or_raise(phone)
        self.phones.remove(phone_obj)

    def edit_phone(self, old_phone:str, new_phone:str)-> None:
        phone_obj = self.__get_phone_or_raise(old_phone)
        phone_obj.value = Phone(new_phone).value

    def find_phone(self, phone:str)-> Phone|None:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def show_birthday(self):
        return f"Contact: {self.name.value}, birthday: {self.birthday.value}"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



