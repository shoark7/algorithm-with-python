def get_cycle_len(d):
    n = 1
    remains = [0] * d
    first_checked = {}
    sequences = []

    i = 0
    while True:
        share, remain = divmod(n, d)

        if not remain:
            return 0
        elif remains[remain]:
            length = i - first_checked[remain]
            sequences.append(share)
            # return sequences[-length:]
            return length
        else:
            first_checked[remain] = i
            remains[remain] = 1
            sequences.append(share)
            n = remain * 10
            i += 1


if __name__ == '__main__':
    SIZE = 1000
    ans = -1
    tmp_max = -1

    for n in range(1, SIZE+1):
        if get_cycle_len(n) > tmp_max:
            ans = n
            tmp_max = get_cycle_len(n)
