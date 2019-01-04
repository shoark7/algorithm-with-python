"""We check if a DIRECTED graph has a cycle or not"""


def has_cycle(graph):
    N = len(graph)
    discovered = [-1] * N
    counter = 0
    finished = [0] * N
    found = False

    def search(here):
        nonlocal counter, found, finished
        if found:
            return
        discovered[here] = counter
        counter += 1

        for there in range(N):
            if graph[here][there]:
                # there is a tree edge. We continue searching
                if discovered[there] == -1:
                    search(there)

                # if there was found earlier than here and finished[there] is 0,
                # it means search(there) function call is not finished and there is parent node of
                # here
                if discovered[here] > discovered[there] and not finished[there]:
                    found = True
                    return

        finished[here] = 1


    for i in range(N):
        if discovered[i] == -1:
            search(i)

    return found


if __name__ == '__main__':

    # Test 1
    N = 5
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[2][3] = 1
    g[3][4] = 1
    g[4][2] = 1

    print(has_cycle(g))

    # Test 2.
    N = 3
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[3][2] = 1
    print(has_cycle(g))

    # Test 3.
    N = 3
    g = [[0] * (N+1) for _ in range(N+1)]

    g[1][2] = 1
    g[2][1] = 1
    g[3][2] = 1
    g[3][1] = 1
    print(has_cycle(g))

    # Test 4.
    N = 7
    g = [[0] * (N+1) for _ in range(N+1)]

    g[0][1] = 1
    g[1][2] = 1
    g[0][4] = 1
    g[4][2] = 1
    g[0][5] = 1
    g[5][3] = 1
    g[5][6] = 1
    g[0][6] = 1
    g[6][3] = 1

    # Without this edge, it loses its cycle
    g[2][0] = 1
    print(has_cycle(g))

    # Test 5.
    N = 1
    g = [[0] * (N+1) for _ in range(N+1)]
    print(has_cycle(g))
