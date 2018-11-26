"""Return the minimal time of finishing lunch time

:input:
2
3
2 2 2
2 2 2
3
1 2 3
1 2 1

:return:
8
7
"""
def min_time(pairs):
    ret, begin_eat = 0, 0
    # pairs: list of (e, h)
    for i in range(len(pairs)):
        begin_eat += pairs[i][1]
        ret = max(ret, begin_eat + pairs[i][0])
    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        H = [int(n) for n in input().split()]
        E = [int(n) for n in input().split()]
        pairs = [(e, h) for e, h in zip(E, H)]
        pairs.sort(reverse=True)
        ans.append(min_time(pairs))

    for n in ans:
        print(n)
