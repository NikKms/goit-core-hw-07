from field import Field


class Phone(Field):
    def __init__(self, value:str)-> None:
        if not value.isnumeric():
            raise ValueError("Phone number must contain numbers only.")
        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)