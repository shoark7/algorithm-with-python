"""Get minimal number of semesters to graduate

:input:
2
4 4 4 4
0
1 0
3 0 1 3
0
4 0 1 2 3
4 0 1 2 3
3 0 1 3
4 0 1 2 3
4 2 2 4
1 1
0
1 3
1 2
3 0 2 3
3 1 2 3

:return:
3
IMPOSSIBLE

url: https://algospot.com/judge/problem/read/GRADUATION
ID : GRADUATION
"""
INF = 987654321

def bit_count(n):
    if n % 2 == 0:
        return 0
    return 1 + bit_count(n // 2)


def min_semester(MIN_REQUIRED, prerequisite, classes_open, limit):
    N, M = len(prerequisite), len(classes_open)
    cache = [[-1 for _ in range(1 << N)] for _ in range(M)]

    def graduate(semester, taken):
        if bit_count(taken) >= MIN_REQUIRED:
            return 0
        elif semester == M:
            return INF
        elif cache[semester][taken] != -1:
            return cache[semester][taken]

        ret = INF
        can_take = classes_open[semester] & ~taken

        for i in range(N):
            if (can_take & (1 << i)) and (taken & prerequisite[i]) != prerequisite[i]:
                can_take &= ~(1 << i)

        take = can_take
        while take > 0:
            if bit_count(take) > limit:
                continue
            ret = min(ret, graduate(semester+1, taken | take) + 1)
            take = (take-1) & can_take

        ret = min(ret, graduate(semester+1, taken))
        cache[semester][take] = ret
        return ret

    return graduate(0, 0)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, K, M, L = (int(n) for n in input().split())
        prerequisite = [0 for _ in range(N)]
        classes_open = [0 for _ in range(M)]

        for i in range(N):
            line = [int(n) for n in input().split()[1:]]
            for c in line:
                prerequisite[i] |= (1 << c)

        for i in range(M):
            line = [int(n) for n in input().split()[1:]]
            for c in line:
                classes_open[i] |= (1 << c)

        ans.append(min_semester(K, prerequisite, classes_open, L))

    for n in ans:
        print('IMPOSSIBLE' if n == INF else n)
