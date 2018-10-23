"""Breakout of Dr. Duniok

ID : NUMB3RS
url: https://algospot.com/judge/problem/read/NUMB3RS
"""
import sys
get = sys.stdin.readline


"""Bottom-up way recursion"""
def prob_in_there(base, target, days):
    cache = [[-1 for _ in range(len(adjacent_matrix))] for _ in range(days+1)]

    # 부분문제 find(d, here): d일 후 here에 있을 때, 최종적으로 days일 때 target에 있을 확률
    def find(passed, here):
        if days == passed:
            return 1 if here == target else 0
        elif cache[passed][here] != -1:
            return cache[passed][here]

        ret = 0
        for there in range(len(cache[0])):
            if adjacent_matrix[there][here]:
                ret += find(passed+1, there)
        ret /= degrees[here]
        cache[passed][here] = ret
        return ret

    return find(0, base)


"""Top-down recursion"""
def prob_in_there(base, target, days):

    # find(d, here): d일 째에 here에 있을 확률
    def find(here, time):
        if time == 0:
            return 1 if here == base else 0
        elif cache[time][here] != -1:
            return cache[time][here]
        else:
            ret = 0
            for there in range(len(adjacent_matrix)):
                if adjacent_matrix[there][here]:
                    ret += find(there, time-1) / degrees[there]
            cache[time][here] = ret
            return ret
    return find(target, days)


if __name__ == '__main__':
    C = int(get())
    ans = []

    for _ in range(C):
        N, D, start = (int(n) for n in get().split())
        adjacent_matrix = []
        degrees = []
        cache = [[-1 for _ in range(N)] for _ in range(D+1)]

        for _ in range(N):
            line = [int(x) for x in get().split()]
            adjacent_matrix.append(line)
            degrees.append(sum(line))

        get()
        targets = [int(x) for x in get().split()]
        ret = []
        for t in targets:
            ret.append(str(prob_in_there(start, t, D)))

        ans.append(' '.join(ret))

    for n in ans:
        print(n)
