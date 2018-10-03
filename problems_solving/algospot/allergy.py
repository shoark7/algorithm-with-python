"""Get the number of least menus that satisfy all the members in a party.

url : https://algospot.com/judge/problem/read/ALLERGY
ID  : ALLERGY
"""
import math


def allergy(favor_sets):
    LEN_F = len(favor_sets)
    LEN_M = len(favor_sets[0])
    bit_set = [0 for _ in range(LEN_M)]
    FIT_ALL = 2 ** LEN_F - 1

    for f in range(LEN_F):
        for m in range(LEN_M):
            if favor_sets[f][m] == 1:
                bit_set[m] |= 2 ** f

    def can_serve_all(menus):
        ret = 0
        for m in menus:
            ret |= bit_set[m]

        return True if ret == FIT_ALL else False

    def get_min_menus(menu_subset, food):
        if food == LEN_M:
            return len(menu_subset) if can_serve_all(menu_subset) else math.inf

        ret = get_min_menus(menu_subset, food+1)
        menu_subset.append(food)
        ret = min(ret, get_min_menus(menu_subset, food+1))
        menu_subset.pop()
        return ret

    return get_min_menus([], 0)


C = int(input())
ans = []
for _ in range(C):
    LEN_F, LEN_M = (int(x) for x in input().split())
    friend_names = input().split()
    favors = [[0 for _ in range(LEN_M)] for _ in range(LEN_F)]

    # favors initialization
    for m in range(LEN_M):
        _, *friends = input().split()
        for f in friends:
            favors[friend_names.index(f)][m] = 1

    ans.append(allergy(favors))

for n in ans:
    print(n)
