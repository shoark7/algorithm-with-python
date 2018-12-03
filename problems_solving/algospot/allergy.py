"""Get the number of least menus that satisfy all the members in a party.

:input:
2
4 6
cl bom dara minzy
2 dara minzy
2 cl minzy
2 cl dara
1 cl
2 bom dara
2 bom minzy
10 7
a b c d e f g h i j
6 a c d h i j
3 a d i
7 a c f g h i j
3 b d g
5 b c f h i
4 b e g j
5 b c g h i

:return:
2
3

url : https://algospot.com/judge/problem/read/ALLERGY
ID  : ALLERGY
"""
def min_menu_required(eater_of, i_can_eat):
    """Return the least number of menus required to satisfy all our friends

    :input:
        eater_of : A list of lists of friends who can eat those menus
        i_can_eat: A list of lists of menus that each friend can eat

    :return:
        An integer of least number of menus required
    """
    N, M = len(i_can_eat), len(eater_of)
    # edible: An temporary list of status of friends. Each element means number of menus a friend can eat
    # with chosen menus
    edible = [0 for _ in range(N)]
    best = 99999

    def search(edible, chosen):
        nonlocal best
        if chosen >= best:
            return

        first = 0
        while first < N and edible[first] > 0:
            first += 1

        if first == N:
            best = chosen
            return

        for m in range(len(i_can_eat[first])):
            food = i_can_eat[first][m]
            for j in range(len(eater_of[food])):
                edible[eater_of[food][j]] += 1
            search(edible, chosen+1)
            for j in range(len(eater_of[food])):
                edible[eater_of[food][j]] -= 1

    search(edible, 0)
    return best


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N, M = (int(n) for n in input().split())
        eater_of = []
        i_can_eat = [[] for _ in range(N)]
        names = [name for name in input().split()]

        for _ in range(M):
            eater_of.append([names.index(name) for name in input().split()[1:]])

        for i in range(len(eater_of)):
            for f in eater_of[i]:
                i_can_eat[f].append(i)

        ans.append(min_menu_required(eater_of, i_can_eat))


    for n in ans:
        print(n)
