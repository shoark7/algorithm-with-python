from collections import Counter


def is_pandigital(num, MIN_V, MAX_V):
    counter = Counter(str(num))

    if all(counter[str(n)] >= 1 for n in range(MIN_V, MAX_V+1)):
        return True
    else:
        return False


def multiply_from_1(n, MIN_LENGTH):
    ret = ''
    m = 1

    while len(ret) < MIN_LENGTH:
        ret += str(n * m)
        m += 1

    return int(ret)


if __name__ == '__main__':
    ans = -1
    for n in range(1, 10 ** 5):
        cand = multiply_from_1(n, 9)
        if is_pandigital(cand, 1, 9) and len(str(cand)) == 9:
            ans = max(ans, int(cand))

    print(ans)
