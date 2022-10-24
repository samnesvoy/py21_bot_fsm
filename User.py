from utilites import MyStates


class User:
    telegram_id = 0
    name = 'name'
    age = 0
    email = 'email'
    state = ''

    def __init__(self, telegram_id: int):
        self.state = MyStates.STATE_0
        self.telegram_id = telegram_id
        # self.name = name
        # self.age = age
        # self.email = email

    def __int__(self):
        return self.telegram_id

    def __str__(self):
        return f'{self.name} {self.age} {self.email}'

    def __eq__(self, other):
        return other == self.telegram_id
