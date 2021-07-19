from unittest.mock import MagicMock, Mock, patch, call


# 1 Mock Patching Methods #################################################
# заменяем метод
class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass


real = ProductionClass()
real.something = MagicMock()  # заменяю функцию в классе на экземпляр MagicMock()
real.method()  # вызываю эту функцию
# проверяем, что эта функция вызвалась 1 раз с аргументами 1,2,3
# при этом мы НЕ заходим внутрь первоначальной функции something(), так как мы
# ее заменили на экземпляр MagicMock()
real.something.assert_called_once_with(1, 2, 3)


# 2 Mock for Method Calls on an Object #################################################
# Заменяем вызов метода
class ProductionClass:
    def closer(self, something):
        something.close()


# Помещаем объект mock в метод closer
real = ProductionClass()
mock = Mock()  # создаю экземпляр класса Mock()
real.closer(mock)  # помещаю mock внутрь closer
mock.close.assert_called_with()  # проверяю что mock вызвался close

# 3 Mocking Classes #################################################
# заменяем класс
# ДОБАВИТЬ ПРИМЕР


# 4 Другое
# даём имя макету
mock = MagicMock(name='foo')

# # Отслеживаем вызовы mock
# pront(mock.mock_calls)

# # вызываем методы, чтобы сравнить их порядок и содержание с mock.mock_calls
# expected = [call.method(), call.attribute.method(10, x=53)]
# print(mock.mock_calls == expected)

# Установить возвращаемое значение
mock.method.return_value = 3
mock.x = 3

# Вызов исключения
mock = Mock(side_effect=Exception('Boom!'))
mock()