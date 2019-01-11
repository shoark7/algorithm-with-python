"""Return number of gifts for children in Christmas day

:input:
5
1 7 0
1 10 1
0 7 3
345 9997 3333
35 9 8

:return:
111111
11
IMPOSSIBLE
35355353545
35


url: https://algospot.com/judge/problem/read/CHILDRENDAY
ID : CHILDRENDAY
"""
def append(here, edge, mod):
    there = here * 10 + edge
    if there >= mod:
        return mod + there % mod
    return there % mod


def gifts(digits, n, m):
    digits = sorted(digits)
    parents = [-1] * n * 2
    choice = [-1] * n * 2
    queue = [0]
    parents[0] = 0

    while queue:
        here = queue.pop(0)
        for d in digits:
            there = append(here, int(d), n)
            if parents[there] == -1:
                parents[there] = here
                choice[there] = d
                queue.append(there)

    if parents[n+m] == -1:
        return "IMPOSSIBLE"

    ret = ''
    here = n + m
    while parents[here] != here:
        ret += choice[here]
        here = parents[here]

    return ret[::-1]


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        d, n, m = (int(n) for n in input().strip().split())
        ans.append(gifts(str(d), n, m))

    for n in ans:
        print(n)
