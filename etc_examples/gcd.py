"""Euclidean algorithm of 2 integers


Date : 2018/03/29
"""


def gcd(a, b):
    s, b = min(a, b), max(a, b)
    return b if s == 0 else gcd(s, b % s)
