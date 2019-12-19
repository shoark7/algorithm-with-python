from math import log10


SIZE = 10 ** 6
sieve = [1] * (SIZE + 1)
sieve[0] = sieve[1] = 0

SQRT_SIZE = int(SIZE ** (1/2))

for i in range(2, SQRT_SIZE+1):
    if sieve[i]:
        for j in range(i*i, SIZE+1, i):
            sieve[j] = 0


def is_circular_prime(n):
    global sieve

    log = int(log10(n))
    for _ in range(log+1):
        if not sieve[n]:
            return False

        n, rest = divmod(n, 10)
        n += rest * 10 ** log

    return True


if __name__ == '__main__':
    count = 0

    for n in range(2, SIZE+1):
        if is_circular_prime(n):
            count += 1
