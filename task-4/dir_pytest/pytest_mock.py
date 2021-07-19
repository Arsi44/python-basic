import pytest

from doctest_example import kth_stat


@pytest.mark.parametrize(
    ('values', 'stat_order', 'expected'), [
        ([1], 1, 1),
        ([1, 1, 1, 1, 1], 4, 3),
        (range(100), 4, 3),
    ]
)
def test_on_range(values, stat_order, expected):
    assert kth_stat(values, stat_order) == expected
