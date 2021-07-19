import random
from doctest_example import kth_stat


def test_on_range():
    assert kth_stat(range(10), 3) == 2


def test_on_shuffled_range():
    li = list(range(10))
    random.shuffle(li)
    assert kth_stat(li, 3) == 2
