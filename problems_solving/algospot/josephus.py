"""Get locations to be last two men standing

:input:
2
6 3
40 3

:return:
3 5
11 26

url: https://algospot.com/judge/problem/read/JOSEPHUS
ID : JOSEPHUS
"""
def not_effective_last_men_standing_by_park(N, K):
    alive = N
    check = [1 for _ in range(N+1)]

    check[0] = check[1] = 0
    alive -= 1
    last = 1
    ans = []

    while alive > 2:
        skip = K
        i = 0

        while skip != 0:
            if check[(last+i) % N+1] == 1:
                skip -= 1
            i += 1
        i -= 1

        check[(last+i) % N+1] = 0
        last = (last+i) % N + 1
        alive -= 1

    for i, n in enumerate(check):
        if n == 1:
            ans.append(i)

    return ans


def last_men_standing(N, K):
    hit_list = [i+1 for i in range(N)]
    kill = 0
    survivor = N

    while survivor > 2:
        hit_list.pop(kill)
        survivor -= 1

        if kill == survivor:
            kill = 0

        for _ in range((K-1) % survivor):
            kill += 1
            if kill == survivor:
                kill = 0

    return hit_list


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, K = (int(n) for n in input().split())
        ans.append(last_men_standing(N, K))

    for n in ans:
        print(' '.join(str(l) for l in n))
