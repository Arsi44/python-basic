import sys

import pytest

from doctest_example import kth_stat


def test_raises():      # Показываем, что мы ожидаем исключение
    with pytest.raises(AssertionError):
        kth_stat(1, 0)


@pytest.mark.xfail()      # Разрешаем тесту падать
def test_raises():
    kth_stat([1, 2, 3], 100)  # <-- тут неверное условие


@pytest.mark.skipif(      # Пропускаем по условию
    sys.platform == 'darwin',
    reason='Change OS'
)
def test_not_to_run_on_darwin():
    print(' -- This is not Mac')


@pytest.mark.skip()      # Пропускаем без условия
def test_not_to_run_on_darwin():
    print('Skipped')
