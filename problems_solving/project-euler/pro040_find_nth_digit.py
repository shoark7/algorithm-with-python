MAX_DIGIT = 10 ** 6

digits_lens = [0]
digits_lens_cum = [1]
e = 1

while digits_lens[-1] <= MAX_DIGIT:
    digits_lens.append(e * 9 * (10 ** (e-1)))
    digits_lens_cum.append(digits_lens_cum[-1] + digits_lens[-1])
    e += 1


def find_nth_digit(nth):
    for e in range(len(digits_lens_cum)):
        if digits_lens_cum[e] <= nth < digits_lens_cum[e+1]:
            break

    d = e + 1
    start = 10 ** e
    cnt, rest = divmod(nth - digits_lens_cum[e], d)
    last = start + cnt
    return str(last)[rest]


if __name__ == '__main__':
    ans = 1
    for e in range(7):
        ans *= int(find_nth_digit(10 ** e))

    print(ans)
