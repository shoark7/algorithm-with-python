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


# Matrix mulplication
def fibonacci_matrix(n):
    BASE = [[1, 1], [1, 0]]
    ZERO = [[1, 0], [0, 1]]
    L = 2
    k = 0
    while 2 ** k <= n:
        k += 1
    k -= 1
    rest = n - 2 ** k

    if n == 0:
        return ZERO
    elif n == 1:
        return BASE


    def two_by_two(a, b):
        L = 2
        tmp = [[0, 0], [0, 0]]
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    tmp[i][j] += a[i][k] * b[k][j]
        return tmp


    def _k_th_matrix(k):
        base = BASE.copy()
        for _ in range(k):
            base = two_by_two(base, base)

        return base

    matrix = _k_th_matrix(k)
    print(matrix)

    if rest == 0:
        return matrix
    else:
        return two_by_two(matrix, fibonacci_matrix(rest))


def fibonacci_matrix(n, __cache={1: [[1, 1], [1, 0]],
                                 0: [[1, 0], [0, 1]],
                                }):

    def matrix_mul(a, b):
        new = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    new[i][j] += a[k][j] * b[i][k]
        return new

    def get_matrix(n):
        if n in __cache:
            return __cache[n]

        m = matrix_mul(get_matrix(n//2), get_matrix(n//2))
        if n % 2 == 1:
            m = matrix_mul(__cache[1], m)
        __cache[n] = m
        return m

    return get_matrix(n)[1][0]
