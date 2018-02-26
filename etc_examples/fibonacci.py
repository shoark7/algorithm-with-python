"""Fibonacci sequence in Python

Get nth number of Fibonacci sequence.
My fibonacci starts with <strong>INDEX 1</strong>.

I used two main ways to implement fibonacci number:
    1. Recursive way: This is formal and simple
    2. Memoization  : Cache way.
                      One used function-internal cache,
                      the other used class-based cache.
"""


# Recursive way
def fibonacci(nth):
    a = 0
    b = 1
    for _ in range(nth - 1):
        a, b = b, a + b

    return a


# Memoization 1. Using function-internal cache
def fibonacci_cache(nth, _cache={1: 0, 2: 1}):
    if nth in _cache:
        return _cache[nth]
    else:
        _cache[nth] = fibonacci_cache(nth-1) + fibonacci_cache(nth-2)
        return _cache[nth]


# Memoization 2. Using class-based cache
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, nth):
        if nth in self.cache:
            return self.cache[nth]
        else:
            self.cache[nth] = self.func(nth)
            return self.cache[nth]


@Memoize
def fibonacci_cache2(nth):
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    else:
        return fibonacci_cache2(nth-1) + fibonacci_cache2(nth-2)
