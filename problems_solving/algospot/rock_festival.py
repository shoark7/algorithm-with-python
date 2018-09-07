"""Find series of days which minimizes the average cost.


ID : FESTIVAL
https://algospot.com/judge/problem/read/FESTIVAL
"""
C = int(input())
min_lists = []
MAX_N = 1000

def get_min_avg(N, L, costs):
    min_ave = MAX_N + 1
    for l in range(L, N+1):
        tmp = sum(costs[:l]) / l
        min_ave = min(min_ave, tmp)
        for i in range(N-l):
            tmp = tmp - costs[i] / l + costs[i+l] / l
            min_ave = min(tmp, min_ave)

    return min_ave


for _ in range(C):
    N, L = (int(x) for x in input().split())
    costs = [int(x) for x in input().split()]
    min_avg = get_min_avg(N, L, costs)

    min_lists.append(min_ave)
