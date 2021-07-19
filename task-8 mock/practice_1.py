from unittest.mock import MagicMock, Mock, patch, create_autospec


class ProductionClass:
    pass


thing = ProductionClass()
# устанавливаем метод и полученное из него значение
thing.method = MagicMock(return_value=3)  # Вызов этого значения: thing.method.return_value
# Вызываем метод с каким-то значением (а именно: 3, 4, 5, key='value')
thing.method(3, 4, 5, key='value')
# Проверяем, что метод был вызван именно со значениями 3, 4, 5, key='value',
# Иначе будет ошибка
thing.method.assert_called_with(3, 4, 5, key='value')


# side_effect позволяет выполнять побочные эффекты, в том числе вызывать исключение при вызове макета:
mock = Mock(side_effect=KeyError('foo'))
mock()  # Traceback ... KeyError: 'foo'

#  Делаем отдельную функцию для применения эффекта side_effect
values = {'a': 1, 'b': 2, 'c': 3}

def side_effect_func(arg):
    return values[arg]

mock.side_effect = side_effect_func
print(mock('a'), mock('b'), mock('c'))  # (1, 2, 3)

# Длаем итератор, основанный на side_effect
mock.side_effect = [5, 4, 3, 2, 1]
print(mock(), mock(), mock())  # (5, 4, 3)


# Декоратор / диспетчер контекста @patch() упрощает имитацию классов или объектов в тестируемом модуле.
# ! См. another_mock_example_1 !

# Меняем словарь ТОЛЬКО на свремя выполнения теста, а после возвращаем его в исходное положение
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}

assert foo == original   # no Traceback


#  Меняем магический метод  __str__
mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
str(mock)  # foobarbaz



# Чтобы гарантировать, что фиктивные объекты в ваших тестах имеют тот же API,
# что и объекты, которые они заменяют, вы можете использовать create_autospec
# Это гарантирует, что ваши макеты выйдут из строя так же, как и ваш производственный код,
# если они будут использоваться неправильно:
def function(a, b, c):
    pass

mock_function = create_autospec(function, return_value='fishy')
mock_function(1, 2, 3)  # 'fishy'
mock_function.assert_called_once_with(1, 2, 3)
mock_function('wrong arguments')  # Error


