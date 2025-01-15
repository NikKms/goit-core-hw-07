from datetime import datetime

from field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


    def __str__(self):
        return f'{self.value.strftime('%d.%m.%Y')}'