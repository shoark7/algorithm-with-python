def desc_n(n):
    skip = n
    ans = []

    def find(chosen, d):
        nonlocal ans, skip

        if skip < 0:
            return
        if len(chosen) == d:
            if skip == 0:
                ans = chosen.copy()
            skip -= 1
            return

        last = chosen[-1]
        for j in range(last):
            chosen.append(j)
            find(chosen, d)
            chosen.pop()

    for d in range(1, 11):
        for i in range(10):
            find([i], d)
        if skip < 0:
            break

    return ans


print(''.join([str(n) for n in ans]) if ans else '-1')
