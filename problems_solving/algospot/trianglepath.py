"""Get the max sum of all possible paths in a triangle


url: https://algospot.com/judge/problem/read/TRIANGLEPATH
ID : TRIANGLEPATH
"""
def max_path_sum(triangle):
    length = len(triangle)
    cache = [[-1 for _ in range(length)] for _ in range(length)]

    def sub_sum(y, x):
        if y == length - 1:
            return triangle[y][x]
        elif cache[y][x] != -1:
            return cache[y][x]
        else:
            cache[y][x] = max(sub_sum(y+1, x), sub_sum(y+1, x+1)) + triangle[y][x]
            return cache[y][x]

    return sub_sum(0, 0)


C = int(input())
ans = []
for _ in range(C):
    N = int(input())
    triangle = []
    for _ in range(N):
        triangle.append([int(x) for x in input().split()])
    ans.append(max_path_sum(triangle))


for n in ans:
    print(n)
