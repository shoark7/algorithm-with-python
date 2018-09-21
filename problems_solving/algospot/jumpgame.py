"""Check if you can reach the last point of the matrix from the 0, 0 point

ID : JUMPGAMe
URL: https://algospot.com/judge/problem/read/JUMPGAME
"""
def jump(y, x):
    global cache
    if y >= N or x >= N:
        return 0
    if y == N - 1 and x == N - 1:
        return 1
    if cache[y][x] != -1:
        return cache[y][x]
    d = matrix[y][x]
    cache[y][x] = jump(y+d, x) or jump(y, x+d)
    return cache[y][x]


C = int(input())
ans = []

for _ in range(C):
    N = int(input())
    matrix = []
    cache = [[-1 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        matrix.append([int(x) for x in input().split()])
    ans.append('YES' if jump(0, 0) else 'NO')

for a in ans:
    print(a)
