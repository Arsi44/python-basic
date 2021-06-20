from my_exceptions import NegativeValueException


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if not isinstance(age, int):
            raise ValueError('Age must be integer')
        if age < 0:
            raise NegativeValueException(self.age)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.age)
