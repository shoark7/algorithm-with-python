"""Return the minimal number of soliders need to cover all ramparts of the city

:input:
3
10
7.02066050 -3.83540431 4.0
-7.23257714 -3.41903904 2.0
0.00000000 -8.00000000 8.0
-8.00000000 -0.00000000 4.8
-6.47213595 4.70228202 3.2
-4.70228202 6.47213595 4.8
7.60845213 -2.47213595 1.6
-2.47213595 -7.60845213 8.8
6.47213595 4.70228202 7.6
-0.00000000 8.00000000 4.8
4
8.00000000 0.00000000 8.00
0.00000000 -8.00000000 8.00
-8.00000000 -0.00000000 8.00
1.25147572 7.90150672 5.40
1
8 0 15.99

:return:
5
4
IMPOSSIBLE

url: https://algospot.com/judge/problem/read/MINASTIRITH
ID : MINASTIRITH
"""
import math


def num_guards(points):
    # points: | A list of (y, x, r) tuple
    rngs = []

    def convert_to_range():
        for y, x, r in points:
            loc = math.atan2(y, x) + math.pi
            rng = 2.0 * math.asin(r / 2.0 / 8.0)
            rng.append(loc-rng, loc+rng)
        rng.sort()

    convert_to_range()
    



if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        points = []
        for _ in range(N):
            y, x, r = (float(n) for n in input().split())
            points.append((y, x, r))
        ans.append(num_guards(points))

    for n in ans:
        print(n)

