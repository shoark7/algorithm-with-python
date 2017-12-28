"""Sieve of Eratosthenes algorithm in Python

This code implements sieve of eratosthenes algorithm.
It returns prime numbers from 2 to n.
I didn't put input validation code for minimalism.


2017/12/28
"""


def eratosthenes(n):
    checked = [1 for _ in range(n+1)]

    for i in range(2, n+1):
        if checked[i]:
            count = 2
            while i * count <= n:
                checked[i * count] = 0
                count += 1

    return [i for i in range(2, n+1) if checked[i]]


if __name__ == '__main__':
    eratosthenes(100)
