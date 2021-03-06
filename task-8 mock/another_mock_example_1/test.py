from unittest import TestCase
from unittest.mock import patch
from main import Calculator


# в строке @patch('main.Calculator.sum', return_value=9)
# мы прописываем явно, что у нас возвращаемое значение ВСЕГДА будет равно 9
# так как мы заменили функцию sum() на пустышку.

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)


# в классе, который мы тестируем должен быть метод 'method'
# прописываем метод и подменяем и подменяем его
with patch.object(Calculator, 'method', return_value=None) as mock_method:
    thing = Calculator()
    thing.method(1, 2, 3)

# проверяем, что метод вызывается со значениями (1, 2, 3)
mock_method.assert_called_once_with(1, 2, 3)


###############################################################################################

# Применяем side_effect в классе для тестирования, заменяем функцию sum из импортированного класса на функцию mock_multi
# и проверяем значение с помощью assert
def mock_multi(a, b):
    return a * b


class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_multi)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 6)
        self.assertEqual(sum(7, 3), 21)
