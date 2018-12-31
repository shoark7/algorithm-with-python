"""Get right order of ancient alphabets

:input:
3
3
ba
aa
ab
5
gg
kia
lotte
lg
hanhwa
6
dictionary
english
is
ordered
ordinary
this

:return:
INVALID HYPOTHESIS
ogklhabcdefijmnpqrstuvwxyz
abcdefghijklmnopqrstuvwxyz

:url:
https://algospot.com/judge/problem/read/DICTIONARY
"""
def get_right_order(words):
    N = 26
    orders = []
    visited = [0] * N
    ans = ''

    def dfs(graph, here):
        nonlocal ans
        visited[here] = 1

        for there in range(N):
            if graph[here][there] and not visited[there]:
                dfs(graph, there)

        orders.append(here)

    def make_graph(words):
        ret = [[0] * N for _ in range(N)]

        for j in range(1, len(words)):
            i = j - 1

            for a, b in zip(words[i], words[j]):
                if a == b:
                    continue
                else:
                    a = ord(a) - ord('a')
                    b = ord(b) - ord('a')
                    ret[a][b] = 1
                    break
        return ret

    g = make_graph(words)

    def topological_sort(graph, orders):
        for i in range(N):
            if not visited[i]:
                dfs(graph, i)

        orders = orders[::-1]

        for i in range(len(orders)):
            for j in range(i+1, len(orders)):
                if g[orders[j]][orders[i]]:
                    return "INVALID HYPOTHESIS"
        return ''.join([chr(ord('a') + n) for n in orders])

    return topological_sort(g, orders)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N = int(input())
        words = []
        for _ in range(N):
            words.append(input())

        ans.append(get_right_order(words))

    for n in ans:
        print(n)
