class MetaClass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        print('name:', name)
        print('bases:', bases)
        print('dct:', dct)
        print('args:', args)
        print('kwargs:', kwargs)
        current_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        print('Created new class:', current_cls)
        return current_cls

ChildClass_1 = MetaClass('ChildClass_1', (), {})
ChildClass_2 = MetaClass('ChildClass_2', (ChildClass_1, ), {'key':'value'})