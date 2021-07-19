import pytest


# Фикстура выполняется 1 раз на модуль (Только 1 раз, при повторном вызове НЕ выполняется)
@pytest.fixture(scope='module')
def module_fixture():
    print('Module fx')


@pytest.fixture()  # Фикстура выполняется по вызову
def every_time_fixture():
    print('Every time fx')


@pytest.fixture(autouse=True)  # Фикстура выполняется всегда, даже если мы её не вызываем
def every_rime_fixture():
    print('Auto use fx')


def test_one(module_fixture, every_time_fixture):
    print('test one')


def test_two(module_fixture, every_time_fixture):
    print('test two')
