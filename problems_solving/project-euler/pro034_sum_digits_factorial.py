from math import factorial


def sum_digits_factorial(n):
    ret = 0

    while n:
        n, rest = divmod(n, 10)
        ret += factorial(rest)

    return ret


if __name__ == '__main__':
    count = 0

    for n in range(10, 10 ** 7):
        if n == sum_digits_factorial(n):
            count += 1

    print(count)
