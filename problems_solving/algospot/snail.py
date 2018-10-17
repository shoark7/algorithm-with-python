"""Get the possiblity of snail can reach D meters in N day


:input:
    4
    5 4
    5 3
    4 2
    3 2

:return:
    0.9960937500
    0.8437500000
    0.5625000000
    0.9375000000


ID : SNAIL
url: https://algospot.com/judge/problem/read/SNAIL
"""
def can_climb(d, n):
    cache = [[-1 for _ in range(d*2+1)] for _ in range(n)]

    def climb(days, climbed):
        if days == n:
            return 1 if climbed >= d else 0
        if cache[days][climbed] != -1:
            return cache[days][climbed]
        cache[days][climbed] = 0.75 * climb(days+1, climbed+2) \
                               + 0.25 * climb(days+1, climbed+1)
        return cache[days][climbed]

    return climb(0, 0)


if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        d, n = (int(x) for x in input().split())
        ans.append(can_climb(d, n))

    for n in ans:
        print(n)
