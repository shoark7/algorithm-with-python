"""Return number of cases of anagrams of a number that can be divided by given m

:input:
4
321 3
123 3
422 2
12738173912 7

:return:
5
0
2
11033

url: https://algospot.com/judge/problem/read/ZIMBABWE
ID : ZIMBABWE
"""
def zimbabwe(e, m):
    MOD = int(1e9) + 7
    e = str(e)
    sorted_str = ''.join(sorted(e))
    N = len(sorted_str)
    cache = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(1<<N)]

    def price(index, taken, mod, less):
        if index == N:
            return 1 if less & (mod == 0) else 0
        elif cache[taken][mod][less] != -1:
            return cache[taken][mod][less]

        ret = 0
        for nxt in range(N):
            if taken & (1<<nxt) == 0:
                if not less and e[index] < sorted_str[nxt]:
                    continue
                elif nxt > 0 and sorted_str[nxt-1] == sorted_str[nxt] and (taken & (1<<(nxt-1))) == 0:
                    continue

                nxt_taken = taken | (1<<nxt)
                nxt_mod = (mod * 10 + int(sorted_str[nxt])) % m
                nxt_less = less or e[index] > sorted_str[nxt]
                ret += price(index+1, nxt_taken, nxt_mod, nxt_less)
                ret %= MOD

        cache[taken][mod][less] = ret
        return ret

    return price(0, 0, 0, 0)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        e, m = (int(n) for n in input().split())
        ans.append(zimbabwe(e, m))

    for n in ans:
        print(n)
