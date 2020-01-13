#### WARNING ####
### NOT SOLVED ##
### ######## ####


"""Get the maximum number of points located in a single 1D line

url: https://www.acmicpc.net/problem/1619
"""
from collections import namedtuple, Counter
import sys

input = sys.stdin.readline
Point = namedtuple('Point', ['x', 'y'])


def max_points_crossing_line(points):
    P = len(points)
    INF = float('inf')
    line_counter = Counter()

    for i in range(P):
        p1 = points[i]
        for j in range(i+1, P):
            p2 = points[j]
            if p1.x - p2.x == 0:
                gradient = INF
            else:
                gradient = (p1.y - p2.y) / (p1.x - p2.x)
            intercept = p1.y - gradient * p1.x
            line_counter[(gradient, intercept)] += 1

    comb = line_counter.most_common(1)[0][1]

    n = 2
    while True:
        if n * (n - 1) // 2 == comb:
            break
        n += 1

    return n if n >= 3 else -1


if __name__ == '__main__':
    N = int(input())
    points = []
    for _ in range(N):
        x, y = (int(n) for n in input().split())
        p = Point(x, y)
        points.append(p)

    print(max_points_crossing_line(points))
