import traceback


class NegativeValueException(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{0} is negative age'.format(self.value)


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


if __name__ == '__main__':

    # Обрабатываем ошибку
    try:
        Puppy = Dog('Nechay', -5)
        print(Puppy)
    # Ошибка была
    except NegativeValueException as e:
        print('Была вызвана ошибка', traceback.format_exc())
    # except ValueError as e:
    #     print('Была вызвана ошибка ', traceback.format_exc())
    except Exception as e:
        print('Возникла друга ошибка', traceback.format_exc())
    # Ошибки не было
    else:
        pass
    # Выполняется в любом случае
    finally:
        pass
