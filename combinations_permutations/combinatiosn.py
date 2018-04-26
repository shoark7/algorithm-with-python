"""Combinations without replacements in Python


Date: 2018/04/26
"""
def combinations(iterable, r):
    """Make combination without replacement generator

    This functions returns a generator which outputs a tuple one by one
    until meets StopIteration.
    """
    n = len(iterable)
    if n < r:
        return ()
    indices = list(range(r))

    yield tuple(iterable[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - r + i:
                break
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(iterable[i] for i in indices)
        if indices[0] == n - r:
            return
