"""Return the minimum cost of merging chapters into a single file

:input:
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

:return:
300
864

url : https://www.acmicpc.net/problem/11066
"""
import sys
sys.setrecursionlimit(10 ** 9)

def min_merge_cost(chaps):
    length = len(chaps)
    cache = [[-1 for _ in range(length+1)] for _ in range(length+1)]
    cache[1][1:length+1] = chaps
    sub_sum = [0 for _ in range(length+1)]
    for i in range(1, length+1):
        sub_sum[i] = sub_sum[i-1] + cache[1][i]
    
    def merge(r, c):
        if cache[r][c] != -1:
            return cache[r][c]
        ret = 987654321
        cost = sub_sum[r+c-1] - sub_sum[c-1]

        for k in range(1, r):
            ret = min(ret, merge(k, c) + merge(r-k, c+k))
        cache[r][c] = ret + cost
        return cache[r][c]
    return merge(length, 1) - sub_sum[length]


if __name__ == '__main__':
    C = int(input())
    ans = []
    
    for _ in range(C):
        N = int(input())
        chapters = [int(n) for n in input().split()]
        ans.append(min_merge_cost(chapters))
    for n in ans:
        print(n)
