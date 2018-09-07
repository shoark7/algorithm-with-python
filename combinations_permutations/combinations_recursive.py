"""Get combination of series in recursive way"""


def combinations(n, to_pick, picked=[]):
    if to_pick == 0:
        print(picked)
        return
    smallest = 0 if not picked else picked[-1] + 1
    for nxt in range(smallest, n):
        picked.append(nxt)
        combinations(n, to_pick-1, picked)
        picked.pop()


combinations(10, 3)
