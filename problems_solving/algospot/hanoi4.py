"""Return least number of moving discs for wanted state of Hanoi towerr

:input:
3
5
1 1
1 3
2 5 4
1 2
3
1 2
0
2 3 1
0
10
2 8 7
2 5 4
3 6 3 2
3 10 9 1

:return:
10
4
24

url: https://algospot.com/judge/problem/read/HANOI4
ID : HANOI4
"""
MAX_DISC = 12


def get_state(state, index):
    return (state >> (index * 2)) & 3


def set_state(state, index, value):
    return (state & ~(3 << (index * 2))) | (value << (index * 2))


def get_num(discs, state, dest):
    if state == dest:
        return 0

    c = {state: 0}
    queue = [state]

    while queue:
        here = queue.pop(0)
        top = [-1] * 4

        for d in range(discs, 0, -1):
            top[get_state(here, d)] = d

        for i in range(4):
            if top[i] == -1:
                continue
            for j in range(4):
                if i != j and (top[j] == -1 or top[j] > top[i]):
                    there = set_state(here, top[i], j)
                    if c.get(there, -1) != -1:
                        continue
                    c[there] = c[here] + 1
                    if there == dest:
                        return c[there]
                    queue.append(there)
    return -1


def get_num_bidirectional(disc, begin, end):
    def get_sign(x):
        if not x:
            return 0
        return 1 if x > 0 else -1

    def incr(x):
        return x - 1 if x < 0 else x + 1

    if begin == end:
        return 0
    queue = [begin, end]
    c = {begin: 1, end: -1}

    while queue:
        here = queue.pop(0)
        top = [-1, -1, -1, -1]

        for i in range(disc, 0, -1):
            top[get_state(here, i)] = i

        for i in range(4):
            if top[i] == -1:
                continue
            for j in range(4):
                if i != j and (top[j] == -1 or top[j] > top[i]):
                    there = set_state(here, top[i], j)

                    if there not in c:
                        c[there] = incr(c[here])
                        queue.append(there)
                    elif get_sign(c[there]) != get_sign(c[here]):
                        return abs(c[there]) + abs(c[here]) - 1
    return -1


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        DEST = 4 ** (N+1) - 4
        state = 0
        for disc_num in range(4):
            discs = [int(n) for n in input().split()][1:]
            for d in discs:
                state += disc_num * (4 ** d)

        ans.append(get_num_bidirectional(N, state, DEST))

    for n in ans:
        print(n)
