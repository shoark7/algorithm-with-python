"""Find cut vertices in UNDIRECTED graph"""

def find_cut(g, start=None):
    if not start:
        start = 1

    counter = 0
    N = len(g)
    discovered = [-1] * N
    is_cut = [0] * N

    def search(here, is_root=False):
        nonlocal counter
        discovered[here] = counter
        counter += 1
        children = 0
        ret = discovered[here]

        for there in range(N):
            if g[here][there] == 1 and discovered[there] == -1:
                children += 1
                most_deep_parents = search(there)
                if not is_root and most_deep_parents >= discovered[here]:
                    is_cut[here] = True
                ret = min(ret, most_deep_parents)
            elif g[here][there] == 1:
                ret = min(ret, discovered[there])

        if is_root:
            is_cut[here] = (children >= 2)
        return ret


    search(start, is_root=True)
    return is_cut


if __name__ == '__main__':

    # Test 1
    N = 5
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[2][3] = 1
    g[3][2] = 1
    g[3][4] = 1
    g[4][3] = 1
    g[4][2] = 1
    g[2][4] = 1

    print(find_cut(g))

    # Test 2.
    N = 3
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[3][2] = 1
    g[2][3] = 1
    print(find_cut(g))

    # Test 3.
    N = 3
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[3][2] = 1
    g[2][3] = 1
    g[3][1] = 1
    g[1][3] = 1
    print(find_cut(g))

    # Test 4.
    N = 7
    g = [[0] * (N+1) for _ in range(N+1)]

    g[0][1] = 1
    g[1][0] = 1
    g[1][2] = 1
    g[2][1] = 1
    g[0][4] = 1
    g[4][0] = 1
    g[4][2] = 1
    g[2][4] = 1
    g[0][5] = 1
    g[5][0] = 1
    g[5][3] = 1
    g[3][5] = 1
    g[5][6] = 1
    g[6][5] = 1
    g[0][6] = 1
    g[6][0] = 1
    g[6][3] = 1
    g[3][6] = 1

    # Without this edge, it loses its cycle
    g[2][0] = 1
    print(find_cut(g))

    # Test 5.
    N = 1
    g = [[0] * (N+1) for _ in range(N+1)]
    print(find_cut(g))
