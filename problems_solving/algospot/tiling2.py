"""Get the number of cases of ways to cover all the board

Get the answer of mod by 1000000007

:input:
3
1
5
100

:output:
1
8
782204094

ID : TILING2
url: https://algospot.com/judge/problem/read/TILING2
"""
def get_tile_ways(n):
    if n == 1:
        return 1

    cache = [-1 for _ in range(n+1)]
    cache[1] = 1
    cache[2] = 2

    def iterate(n):
        if cache[n] != -1:
            return cache[n]
        cache[n] = iterate(n-1) + iterate(n-2)
        cache[n] %= 1000000007
        return cache[n]

    return iterate(n)


C = int(input())
ans = []
for _ in range(C):
    ans.append(get_tile_ways(int(input())))

for n in ans:
    print(n)
