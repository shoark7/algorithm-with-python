def get_number_ways(num):
    UNITS = [1, 2, 5, 10, 20, 50, 100, 200]
    U = len(UNITS)
    ans = 0
    num *= 100 # 1 pound = 100 pence
               # '달과 6펜스'가 생각남. ㅇㅈ?

    cache = [[0] * (num + 1) for _ in range(U+1)]
    for u in range(U+1):
        cache[u][0] = 1

    UNITS = [0] + UNITS

    for u in range(1, U+1):
        for n in range(num+1):
            if UNITS[u] > n:
                break

            cache[u][n] = cache[u-1][n] + (cache[u][n-UNITS[u]] if n - UNITS[u] >= 0 else 0)

    return cache


if __name__ == '__main__':
    print(get_number_ways(2))
