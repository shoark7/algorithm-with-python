"""Implement Tarjan's SCC condensation algorithm in DIRECTED graph"""

N = 10
graph = [[0] * N for _ in range(N)]
scc_ids = [-1] * N
discovered = [-1] * N
stack = []

scc_counter = 0
vertex_counter = 0


def scc(here):
    ret = discovered[here] = vertex_counter
    vertex_counter += 1
    stack.append(here)

    for there in range(N):
        if graph[here][there] and discovered[there] == -1:
            ret = min(ret, scc(there))
        elif graph[here][there] and scc_id[there] == -1:
            ret = min(ret, discovered[there])

    if ret == discovered[here]:
        while True:
            t = stack.pop()
            scc_id[t] = scc_counter
            if t == here:
                break
        scc_counter += 1

    return ret


def tarjan_scc():
    for i in range(N):
        if not discovered[i] == -1:
            scc(i)

    return scc_id
