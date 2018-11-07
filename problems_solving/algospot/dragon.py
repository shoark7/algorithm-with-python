"""

:input:
4
0 1 2
1 1 5
2 6 5
42 764853475 30

:return:
FX
FX+YF
+FX-Y
FX-YF-FX+YF+FX-YF-FX+YF-FX-YF-
"""
def dragon(seed, generations):
    if generations == 0:
        return seed
    ans = ''

    for i in range(len(seed)):
        if seed[i] == 'X':
            ans += dragon_maker('X+YF', generations-1)
        elif seed[i] == 'Y':
            ans += dragon_maker('FX-Y', generations-1)
        else:
            ans += seed[i]
    return ans


def dragon_maker(seed, generations, p, l):
    EXPAND_X = 'X+YF'
    EXPAND_Y = 'FX-Y'
    len_cache = [-1 for _ in range(generations+1)]
    len_cache[0] = 1
    ans = ''

    for i in range(1, generations+1):
        len_cache[i] = len_cache[i-1] * 2 + 2

    def expand(string, generations, skip):
        if generations == 0:
            return string[skip] if skip < len(string) else ''

        for i in range(len(string)):
            if string[i] == 'X' or string[i] == 'Y':
                if skip >= len_cache[generations]:
                    skip -= len_cache[generations]
                elif string[i] == 'X':
                    return expand(EXPAND_X, generations-1, skip)
                else:
                    return expand(EXPAND_Y, generations-1, skip)
            elif skip > 0:
                skip -= 1
            else:
                return string[i]

    for i in range(l):
        ans += expand(seed, generations, p-1+i)
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        n, p, l = (int(n) for n in input().split())
        ans.append(dragon_maker('FX', n, p, l))

    for n in ans:
        print(n)
