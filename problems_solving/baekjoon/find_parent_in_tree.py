"""Find parent nodes of all nodes in a tree
:input:
7
1 6
6 3
3 5
4 1
2 4
4 7

:return:
4
6
1
3
1
4

url: https://www.acmicpc.net/problem/11725
"""
from sys import stdin


N = int(input())
parent = [None] * (N+1)
parent[1] = 0
visited = [0] * (N+1)
visited[1] = 1
queue = [1]
relations = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b = (int(n) for n in stdin.readline().strip().split())
    relations[a].append(b)
    relations[b].append(a)


while queue:
    x = queue.pop()
    for child in relations[x]:
        if not visited[child]:
            visited[child] = 1
            queue.append(child)
            parent[child] = x


for i in range(2, N+1):
    print(parent[i])
