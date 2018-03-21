"""
10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?
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


def prime_number_generator():
    n = 3
    yield 2
    yield 3

    while True:
        n += 2
        if is_prime(n):
            yield n


prime_sum = 0
p_now = 0
gen = prime_number_generator()

while p_now <= 2000000:
    prime_sum += p_now
    p_now = next(gen)

print(prime_sum)
