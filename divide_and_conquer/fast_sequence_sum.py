"""Get the sum of sequences between 1 to given natural number n.

I will all input is natural number over 0.
"""


def fast_sum(n):

    if n == 1:
        return 1
    elif n % 2 == 1:
        return fast_sum(n-1) + n
    else:
        return n*n // 4 + fast_sum(n//2)
