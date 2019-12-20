from math import log10


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    for d in range(3, int(n ** (1/2))+1, 2):
        if n % d == 0:
            return False

    return True


def move_shift_once(n, is_left=True):
    if is_left:
        log = int(log10(n))
        return n % (10 ** log)
    else:
        return n // 10


if __name__ == '__main__':
    primes = []
    n = 11

    while len(primes) < 11:
        if is_prime(n):
            is_all_prime = True
            log = int(log10(n))
            left_shifted = right_shifted = n

            for _ in range(log):
                left_shifted = move_shift_once(left_shifted)
                right_shifted = move_shift_once(right_shifted, is_left=False)
                if not is_prime(left_shifted) or not is_prime(right_shifted):
                    is_all_prime = False
                    break

            if is_all_prime:
                primes.append(n)

        n += 2


    print(sum(primes))
