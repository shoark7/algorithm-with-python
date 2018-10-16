"""Return the number of paths that maximize the total sum of their elements

:input:
2
4
1
1 1 
1 1 1 
1 1 1 1 
4
9
5 7
1 3 2
3 5 5 6

:return:
8
3

ID : TRIPATHCNT
url: https://algospot.com/judge/problem/read/TRIPATHCNT
"""
def path_count(tri):
    length = len(tri)
    cache = [[-1 for _ in range(length)] for _ in range(length)]
    count_cache = [[-1 for _ in range(length)] for _ in range(length)]

    def find(y, x):
        if y == length - 1:
            return tri[y][x]
        elif cache[y][x] != -1:
            return cache[y][x]
        else:
            cache[y][x] = max(find(y+1, x), find(y+1, x+1)) + tri[y][x]
            return cache[y][x]

    def count(y, x):
        if y == length - 1:
            return 1
        elif count_cache[y][x] != -1:
            return count_cache[y][x]
        else:
            ret = 0
            if find(y+1, x+1) >= find(y+1, x):
                ret += count(y+1, x+1)
            if find(y+1, x+1) <= find(y+1, x):
                ret += count(y+1, x)
            count_cache[y][x] = ret
            return ret
    return count(0, 0)



if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        tri = []
        for _ in range(N):
            tri.append([int(n) for n in input().split()])
        ans.append(path_count(tri))

    for n in ans:
        print(n)
