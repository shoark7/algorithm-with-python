"""Solve algospot picnic problem


ID : PICNIC


https://algospot.com/judge/problem/read/PICNIC

:input:
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

:output:
1
3
4
"""
MAX_N = 10
chosen = [0 for _ in range(MAX_N)]
friends_matrix = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
answer_list = []


def clear_matrix(n, chosen, friends_matrix):
    for i in range(n):
        for j in range(n):
            friends_matrix[i][j] = 0
    chosen = [0 for _ in range(n)]
    return chosen, friends_matrix


def find_couples(n, chosen, friends_matrix):
    ans = 0
    first = -1
    for i in range(n):
        if not chosen[i]:
            first = i
            break
    # 기저 사례 : 모든 조합 완성 시 한 가지 경우의 수 반환
    if first == -1:
        return 1

    for j in range(first+1, n):
        if not chosen[j] and friends_matrix[first][j]:
            chosen[first] = 1
            chosen[j] = 1
            ans += find_couples(n, chosen, friends_matrix)
            chosen[first] = 0
            chosen[j] = 0
    return ans


C = int(input())
for _ in range(C):
    n, m = (int(x) for x in input().split())
    chosen, friends_matrix = clear_matrix(n, chosen, friends_matrix)
    l = [int(x) for x in input().split()]
    for i in range(m):
        a, b = l[i*2], l[i*2+1]
        friends_matrix[a][b] = 1

    answer_list.append(find_couples(n, chosen, friends_matrix))


for n in answer_list:
    print(n)
