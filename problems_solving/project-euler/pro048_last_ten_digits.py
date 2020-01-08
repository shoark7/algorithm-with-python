if __name__ == '__main__':
    ans = 0
    for n in range(1, 1001):
        ans += pow(n, n, 10 ** 10)

    ans %= 10 ** 10

    print(ans)
