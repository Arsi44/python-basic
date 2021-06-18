class MetaClass(type):
    # * Для инициализации классов нужно использовать метод __new__
    def __new__(cls, name, bases, dct, *args, **kwargs):
        dct['dict_key'] = 'dict_value'
        # print('name:', name)
        # print('bases:', bases)
        # print('dct:', dct)
        # print('args:', args)
        # print('kwargs:', kwargs)
        current_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        print('Created new class:', current_cls)
        return current_cls


if __name__ == '__main__':
    # Создаём классы
    ChildClass_1 = MetaClass('ChildClass_1', (), {})
    ChildClass_2 = MetaClass('ChildClass_2', (ChildClass_1,), {'key': 'value'})


    class ChildClass_3(metaclass=MetaClass):
        @staticmethod
        def echo_func(text):
            # * repr - строкове представление объекта, str - читаема строка
            return text

    # Создаем экземпляры классов
    inst_from_1_cls = ChildClass_1()
    inst_from_2_cls = ChildClass_2()
    inst_from_3_cls = ChildClass_3()

    # Получаю значения
    print(inst_from_1_cls.dict_key)
    print(inst_from_2_cls.key, inst_from_2_cls.dict_key)
    print(inst_from_3_cls.dict_key, inst_from_3_cls.echo_func('lalala'))
