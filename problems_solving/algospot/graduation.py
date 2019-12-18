"""Return minimum number of semesters to take to graduate

url: https://algospot.com/judge/problem/read/GRADUATION
ID : GRADUATION
"""
INF = float('inf')


def bit_count(n):
    return (n & 1) + bit_count(n >> 1) if n else 0


def min_semestered_required(K, L, prerequisites, opened_lectures):
    N, S = len(prerequisites), len(opened_lectures)
    cache = [[None] * (1 << N) for _ in range(S)]

    def graduate(semester, taken):
        if bit_count(taken) >= K:
            return 0
        elif semester == S:
            return INF

        if cache[semester][taken] is not None:
            return cache[semester][taken]

        ret = INF

        can_take = opened_lectures[semester] & ~taken

        for i in range(N):
            if (can_take & (1 << i)) \
               and (taken & prerequisites[i]) != prerequisites[i]:
                can_take &= ~(1 << i)

        take = can_take + 1

        while take:
            take = (take - 1) & can_take
            if bit_count(take) <= L:
                ret = min(ret, graduate(semester+1, taken | take) + 1)

        ret = min(ret, graduate(semester+1, taken))
        cache[semester][taken] = ret

        return ret

    ans = graduate(0, 0)

    return ans if ans != INF else "IMPOSSIBLE"


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        N, K, S, L = (int(n) for n in input().strip().split())
        prerequisites = []
        opened_lectures = []

        for _ in range(N):
            pres = [int(n) for n in input().strip().split()[1:]]
            pres_bit = 0

            for p in pres:
                pres_bit |= (1 << p)

            prerequisites.append(pres_bit)

        for _ in range(S):
            lectures = [int(n) for n in input().strip().split()[1:]]
            lec_bit = 0

            for l in lectures:
                lec_bit |= (1 << l)

            opened_lectures.append(lec_bit)

        ans.append(min_semestered_required(K, L, prerequisites, opened_lectures))


    for ret in ans:
        print(ret)

