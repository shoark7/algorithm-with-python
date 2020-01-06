def get_factors(n):
    ret = set()
    d = 3

    while not n % 2:
        ret.add(2)
        n //= 2

    while n != 1:
        while not n % d:
            ret.add(d)
            n //= d
        d += 2

    return ret


if __name__ == '__main__':
    n = 1
    while True:
        if len(get_factors(n)) != 4:
            n += 1
        elif len(get_factors(n+1)) != 4:
            n += 2
        elif len(get_factors(n+2)) != 4:
            n += 3
        elif len(get_factors(n+3)) != 4:
            n += 4
        else:
            print(n)
            break
