"""Euclidean algorithm of 2 integers


Date : 2018/03/30
"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
