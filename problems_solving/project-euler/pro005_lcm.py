"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""
from functools import reduce


def is_prime(n):
    if n == 1:
        return False
    elif n in [2, 3]:
        return True

    for d in range(2, int(pow(n, 1/2))+1):
        if n % d == 0:
            return False
    return True


def prime_number_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def get_lcm(arr):
    generator = prime_number_generator()
    ns = []

    while True:
        prime = next(generator)
        while True:
            changed = False
            for i, n in enumerate(arr):
                if n % prime == 0:
                    arr[i] = n // prime
                    changed = True
            if changed:
                ns.append(prime)
            else:
                break

        if all(n == 1 for n in arr):
            return reduce(lambda x, y: x * y, ns)


print(get_lcm([n for n in range(1, 21)]))
