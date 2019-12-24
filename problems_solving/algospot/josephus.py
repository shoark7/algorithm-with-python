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


def josephus(N, STRIDE, idx_start_from_1=True):
    still_alive = list(range(N))
    kill = 0

    while len(still_alive) > 2:
        still_alive.pop(kill)
        kill = (kill + STRIDE - 1) % len(still_alive)

    if idx_start_from_1:
        return [n + 1 for n in still_alive]
    else:
        return still_alive


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, STRIDE = (int(n) for n in input().split())
        ans.append(josephus(N, STRIDE, idx_start_from_1=True))

    for a, b in ans:
        print(a, b)
