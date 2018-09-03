"""Find series of days which minimizes the average cost.


ID : FESTIVAL
https://algospot.com/judge/problem/read/FESTIVAL
"""
C = int(input())
min_lists = []

for _ in range(C):
    N, L = (int(x) for x in input().split())
    min_ave = 1001
    costs = [int(x) for x in input().split()]

    for l in range(L, N+1):
        tmp = sum(costs[:l]) / l
        min_ave = min(min_ave, tmp)
        for i in range(N-l):
            tmp = tmp - costs[i] / l + costs[i+l] / l
            min_ave = min(tmp, min_ave)

    min_lists.append(min_ave)


for i in range(C):
    print(min_lists[i])
