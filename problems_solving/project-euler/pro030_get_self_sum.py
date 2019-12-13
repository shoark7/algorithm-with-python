def sum_squared_digits(n, d):
    ans = 0
    while n:
        n, rest = divmod(n, 10)
        ans += (rest ** d)

    return ans


if __name__ == '__main__':
    MAX = 10 ** 6
    ans = 0

    for n in range(10, MAX):
        if sum_squared_digits(n, 5) == n:
            ans += n

    print(ans)
