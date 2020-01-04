def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif not n % 2:
        return False

    for d in range(3, int(n ** (1/2))+1, 2):
        if not n % d:
            return False

    return True


def is_composite(n):
    return not is_prime(n) if n != 1 else False


if __name__ == '__main__':
    n = 7
    is_ok = True

    while is_ok:
        n += 2
        if not is_composite(n):
            continue

        is_ok = False
        c = 1

        while n > 2 * (c ** 2):
            left = n - 2 * (c ** 2)
            if is_prime(left):
                is_ok = True
                break

            c += 1


    print(n)
