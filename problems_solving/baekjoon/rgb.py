"""Return minimum cost of painting the roofs of houses in a row

:input:
3
26 40 83
49 60 57
13 89 99

:return:
96
"""
import sys
sys.setrecursionlimit(10 ** 6)

INF = 987654321

def min_cost(arr):
    length = len(arr)
    cache = [[-1 for _ in range(3)] for _ in range(length)]
    colors = 'RGB'
    ans = ['' for _ in range(length)]

    def cal_cost(loc, color):
        if loc < 0:
            return 0
        elif cache[loc][color] != -1:
            return cache[loc][color]

        tmp = INF
        for c in range(3):
            if c != color:
                tmp = min(tmp, cal_cost(loc-1, c) + arr[loc][color])
        cache[loc][color] = tmp
        return tmp

    def nth_min_cost(loc):
        return min(cal_cost(loc, i) for i in range(3))

    def generate(loc, last):
        if loc < 0:
            return ''
        if cal_cost(loc, (last+1) % 3) < cal_cost(loc, (last+2) % 3):
            last = (last + 1) % 3
        else:
            last = (last + 2) % 3
        ans[loc] = colors[last]
        generate(loc-1, last)

    #### If you want to get minimum cost
    return nth_min_cost(length-1)

    #### If you want to get a list of colors that makes up minimum costs
    min_value = nth_min_cost(length-1) + 1
    for i in range(3):
        if cal_cost(length-1, i) < min_value:
            min_value = cal_cost(length-1, i)
            last = i
    ans[length-1] = colors[last]
    generate(length-2, last)
    return ''.join(ans)


if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append([int(n) for n in input().split()])
    print(min_cost(arr))
