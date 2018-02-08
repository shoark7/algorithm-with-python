"""Radix sort in Python


Date: 2018/02/18
"""


def radix_sort(target, reverse=False):
    """Radix sort in Python

    This sort uses 'queue way'. But simply uses list in Python.
    Also it assumes all elements in target are POSITIVE INTEGERS.
    """
    def get_nth_digit(n, d):
        n %= 10 ** d
        return n // 10 ** (d-1)

    digit = 0
    max_value = max(target)
    while max_value:
        digit += 1
        max_value //= 10

    sort_queue = list()
    iter_range = range(10) if not reverse else range(9, -1, -1)

    for d in range(1, digit+1):
        for i in iter_range:
            for n in target:
                if get_nth_digit(n, d) == i:
                    sort_queue.append(n)
        target[:] = sort_queue.copy()  # Can you guess why assignment is like this?
        sort_queue.clear()
    return target
