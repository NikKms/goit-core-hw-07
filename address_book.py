from collections import UserDict
from datetime import datetime

from date_utils import DateUtils
from record import Record


class AddressBook(UserDict):

    def __str__(self):
        result=["AddressBook:"]
        for name, record in self.data.items():
            result.append(f"{name}: {record}")
        return "\n".join(result)

    def add_record(self, record)-> None:
        self.data[record.name.value] = record

    def find(self, name:str)-> Record|None:
        return self.data.get(name, None)

    def delete(self, name: str) -> None | str:
        if self.data.pop(name, None) is None:
            return f"{name} not found in your AddressBook"

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.today()

        for user in self.data.values():
            if not user.birthday:
                continue

            birthday_this_year = datetime.strptime(user.birthday.value, '%d.%m.%Y').replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = DateUtils.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = DateUtils.format_date(birthday_this_year)
                upcoming_birthdays.append({"name": user.name.value, "birthday": congratulation_date_str})

        return upcoming_birthdays
