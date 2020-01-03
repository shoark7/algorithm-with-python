def get_digit(n, start, length):
    n = str(n)
    return n[start-1:start-1+length]


def sum_pandigial():
    LENGTH = 3
    used = [False] * 10
    starts = [2, 3, 4, 5, 6, 7, 8]
    dividers = [2, 3, 5, 7, 11, 13, 17]
    pandigitals = []
    ans = []

    def generate_pandigitals(tmp, used, left):
        nonlocal pandigitals
        if not left:
            pandigitals.append(tmp)
            return

        for n in range(10):
            if not used[n]:
                used[n] = True
                generate_pandigitals(tmp + str(n), used, left-1)
                used[n] = False

    generate_pandigitals('', used, 10)

    for pan in pandigitals:
        if all(int(get_digit(pan, start, LENGTH)) % divider == 0 for start, divider in zip(starts,
                                                                                      dividers)):
            ans.append(int(pan))

    return ans


if __name__ == '__main__':
    ans = sum_pandigial()
    print(ans)
