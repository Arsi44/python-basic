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


