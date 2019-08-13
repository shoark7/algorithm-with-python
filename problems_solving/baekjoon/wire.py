"""Get number of mininum number of single wires not for them to be twisted
:input:
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

:return:
3

url: https://www.acmicpc.net/problem/2565
No : 2565
"""
def min_wire_to_remove(points):
    points.sort(key=lambda x: x[0])
    points = [x[1] for x in points]
    cache = [0] * len(points)
    cache[0] = 1

    for i in range(1, len(points)):
        tmp_ans = 0
        for j in range(i):
            if points[j] < points[i]:
                tmp_ans = max(tmp_ans, cache[j])
        cache[i] = tmp_ans + 1
    return len(points) - max(cache)


if __name__ == '__main__':
    C = int(input())
    points = []
    for _ in range(C):
        c = tuple(int(n) for n in input().split())
        points.append(c)
    print(min_wire_to_remove(points))
