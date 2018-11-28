"""Return the least number of swithces to make all clocks to 12 o'clock

:input:
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6

:return:
2
9

ID : CLOCKSYNC
url: https://algospot.com/judge/problem/read/CLOCKSYNC
"""
import time


SWITCHES = [[0, 1, 2],
            [3, 7, 9, 11],
            [4, 10, 14, 15],
            [0, 4, 5, 6, 7],
            [6, 7, 8, 10, 12],
            [0, 2, 14, 15],
            [3, 14, 15],
            [4, 5, 7, 14, 15],
            [1, 2, 3, 4, 5],
            [3, 4, 5, 9, 13],
           ]


def algospot_n_clock(now):
    stime = time.time()
    N = len(SWITCHES)
    INF = 987654321

    def push(now, switch):
        for t in SWITCHES[switch]:
            now[t] += 3
            if now[t] == 15:
                now[t] = 3

    def solve(now, switch):
        if switch == N:
            return 0 if all(t == 12 for t in now) else INF
        ret = INF

        for cnt in range(4):
            ret = min(ret, cnt + solve(now, switch+1))
            push(now, switch)

        return ret if ret != INF else -1

    ret = solve(now, 0)
    etime = time.time()
    print('-' * 40)
    print('Total time is', etime - stime)
    print('-' * 40)
    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        now = [int(n) for n in input().split()]
        ans.append(solve(now))

    for n in ans:
        print(n)
