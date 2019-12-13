def get_spiral_sums(n):
    ans = 1
    times = (n - 1) // 2
    d = 2
    tmp = 1

    for _ in range(times):
        for _ in range(4):
            tmp += d
            ans += tmp
        d += 2

    return ans


if __name__ == '__main__':
    print(get_spiral_sums(1001))
