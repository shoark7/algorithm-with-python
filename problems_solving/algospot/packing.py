"""Return the combinations of items that minimize the total sum of the volumes

:input:
    2
    6 10
    laptop 4 7
    camera 2 10
    xbox 6 6
    grinder 4 7
    dumbell 2 5
    encyclopedia 10 4
    6 17
    laptop 4 7
    camera 2 10
    xbox 6 6
    grinder 4 7
    dumbell 2 5
    encyclopedia 10 4

:return:
    24 3   <- (sum of volumes, number of itmes)
    laptop
    camera
    grinder
    30 4
    laptop
    camera
    xbox
    grinder


ID : PACKING
url: https://algospot.com/judge/problem/read/PACKING
"""
from collections import namedtuple


def best_packing(items, V):
    length = len(items)
    cache = [[-1 for _ in range(V+1)] for _ in range(length)]
    ans = []

    def max_needs(i, v):
        if i == length:
            return 0
        elif cache[i][v] != -1:
            return cache[i][v]
        ret = max_needs(i+1, v)
        if items[i].vol <= v:
            ret = max(ret, max_needs(i+1, v - items[i].vol) + items[i].needs)
        cache[i][v] = ret
        return ret

    def make_answer(i, v):
        if i == length:
            return
        elif max_needs(i, v) == max_needs(i+1, v):
            make_answer(i+1, v)
        else:
            ans.append(items[i].name)
            make_answer(i+1, v-items[i].vol)

    max_needs(0, V)
    make_answer(0, V)
    return cache[0][V], ans


if __name__ == '__main__':
    C = int(input())
    Item = namedtuple('Item', ['name', 'vol', 'needs'])


    for _ in range(C):
        items = []
        N, MAX_VOLUME = (int(x) for x in input().split())

        for i in range(N):
            items.append(Item(*(int(x) if x.isnumeric() else x for x in input().split())))

        needs, comb = best_packing(items, MAX_VOLUME)
        print(needs, len(comb))
        print('\n'.join(comb))
