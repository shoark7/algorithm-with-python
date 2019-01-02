"""Solve algospot picnic problem

:input:
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

:output:
1
3
4

ID : PICNIC
url: https://algospot.com/judge/problem/read/PICNIC
"""
def get_ways(are_friends):
    N = len(are_friends)
    taken = [0] * N

    def find(left):
        if left == 0:
            return 1

        for i in range(N):
            if not taken[i]:
                nxt = i
                break

        ans = 0
        for i in range(nxt+1, N):
            if not taken[i] and are_friends[i][nxt]:
                taken[i] = 1
                taken[nxt] = 1
                ans += find(left-2)
                taken[i] = 0
                taken[nxt] = 0
        return ans

    return find(N)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        n, m = (int(n) for n in input().split())
        are_friends = [[0] * n for _ in range(n)]
        rels = [int(n) for n in input().split()]
        i = 0

        while i < len(rels):
            are_friends[rels[i]][rels[i+1]] = 1
            are_friends[rels[i+1]][rels[i]] = 1
            i += 2

        ans.append(get_ways(are_friends))

    for n in ans:
        print(n)

