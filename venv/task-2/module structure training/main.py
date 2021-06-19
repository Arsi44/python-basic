import traceback

if __name__ == '__main__':

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
