"""Get the mininum cost of building a wanted building


url: https://www.acmicpc.net/problem/1005
"""
import sys
sys.setrecursionlimit(10 ** 9)


def get_building_time(w, time, rule_cache):
    total_time_cache = [-1 for _ in range(len(time))]

    for i in rule_cache[0]:
        total_time_cache[i] = time[i]

    def get_time(w):
        if total_time_cache[w] == -1:
            ret = -1
            for src in rule_cache[w]:
                ret = max(ret, get_time(src))
            total_time_cache[w] = ret + time[w]
        return total_time_cache[w]
    return get_time(w)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, R = (int(n) for n in input().split())
        time = [0] + [int(n) for n in input().split()]
        rule_cache = [[] for _ in range(len(time))]
        start = [1 for _ in range(len(time))]

        for _ in range(R):
            src, dest = (int(n) for n in input().split())
            rule_cache[dest].append(src)
            start[dest] = 0
        rule_cache[0] = [dest for dest in range(len(time)) if start[dest] == 1]


        W = int(input())
        v = get_building_time(W, time, rule_cache)
        ans.append(v)

    for n in ans:
        print(n)
