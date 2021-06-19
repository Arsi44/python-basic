import traceback
import os
from animals import Dog
from my_exceptions import NegativeValueException

if __name__ == '__main__':
    print(os.getcwd())

    # Обрабатываем ошибку
    try:
        Puppy = Dog('Nechay', -5)
        print(Puppy)
    except NegativeValueException as e:
        print('Была вызвана ошибка', traceback.format_exc())
    except ValueError:
        print('Была вызвана ошибка ValueError')
    except Exception as e:
        print(e)
        print('Возникла друга ошибка', traceback.format_exc())
