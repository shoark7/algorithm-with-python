
"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

def is_prime(n):
    if n == 1:
        return False
    elif n in [2, 3]:
        return True

    for d in range(2, int(pow(n, 1/2))+1):
        if n % d == 0:
            return False
    return True


def nth_prime_number(nth):
    if not isinstance(nth, int) or nth <= 0:
        raise ValueError("nth must be an interger over o")
    elif nth == 1:
        return 2

    count = 2
    n = 3

    while count != nth:
        n += 2
        if is_prime(n):
            count += 1
    return n

print(f'{10001:>2d} : {nth_prime_number(10001):>2d}')
