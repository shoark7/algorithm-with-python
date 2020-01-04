def hex_generator(start=1):
    n = start
    while True:
        yield n * (n + 1) // 2
        n += 1


def penta_generator(start=1):
    n = start
    while True:
        yield n * (3*n - 1) // 2
        n += 1


def trigonal_generator(start=1):
    n = start
    while True:
        yield n * (2*n - 1)
        n += 1


if __name__ == '__main__':
    tri_gen = trigonal_generator(285)
    pen_gen = penta_generator(165)
    hex_gen = hex_generator(144) # 143에서 1 키움

    t, p, h = next(tri_gen), next(pen_gen), next(hex_gen)

    while not (t == p == h):
        min_n = min(t, p, h)
        if min_n == h:
            h = next(hex_gen)
        elif min_n == p:
            p = next(pen_gen)
        else:
            t = next(tri_gen)


    print(t)
