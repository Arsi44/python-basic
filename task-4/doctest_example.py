def kth_stat(iterable, k):
    """Compute k-order stat in iterable
    >>> kth_stat([4,1,0], 1)
    0
    >>> kth_stat(range(100), 20)
    10
    """
    return sorted(iterable)[k - 1]


