"""Return possibilities of songs being played in a specific time

:input:
3
3 6 3
4 4 2
0.18 0.40 0.42
0.15 0.46 0.39
0.58 0.23 0.19
0 1 2
4 10 4
1 3 2 4
0.26 0.07 0.49 0.18
0.21 0.33 0.15 0.31
0.41 0.20 0.38 0.01
0.28 0.31 0.18 0.23
2 0 3 1
4 1000 4
4 3 4 4
0.08 0.47 0.12 0.33
0.10 0.02 0.39 0.49
0.08 0.33 0.35 0.24
0.14 0.19 0.58 0.09
1 3 2 0

:return:
0.42360000 0.49660000 0.07980000
0.31060929 0.13791635 0.26756048 0.28391388
0.18648004 0.28409359 0.42243515 0.10699122
"""
def get_prb(K, wanted, song_length, T):
    N = len(song_length)
    cache = [[0 for _ in range(N)] for _ in range(5)]
    cache[0][0] = 1.0
    probs = [0 for _ in range(N)]
    ret = []

    for time in range(1, K+1):
        for nxt in range(N):
            tmp = 0
            for prev in range(N):
                tmp += cache[(time-song_length[prev]+5) % 5][prev] * T[prev][nxt]
            cache[time % 5][nxt] = tmp

    for song in range(N):
        for start in range(K-song_length[song]+1, K+1):
            probs[song] += cache[start % 5][song]

    for m in wanted:
        ret.append(probs[m])

    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, K, M = [int(n) for n in input().split()]
        T = [None for _ in range(N)]
        song_length = [int(n) for n in input().split()]
        for i in range(N):
            T[i] = [float(n) for n in input().split()]

        wanted = [int(n) for n in input().split()]
        ans.append(get_prb(K, wanted, song_length, T))

    for n in ans:
        print(' '.join(str(c) for c in n))
