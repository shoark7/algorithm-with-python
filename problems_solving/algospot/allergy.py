"""Return minimum number of foods to satisfy all friends

url: https://algospot.com/judge/problem/read/ALLERGY
ID : ALLERGY
"""
def minimum_foods(eaters, FRIEND):
    FOOD = len(eaters)
    best = float('inf')
    edible = [0] * FRIEND
    can_eat = [[] for _ in range(FRIEND)]

    for i in range(len(eaters)):
        for f in eaters[i]:
            can_eat[f].append(i)


    def search(edible, chosen):
        nonlocal best
        if chosen >= best:
            return

        first = 0

        while first < FRIEND and edible[first] > 0:
            first += 1

        if first == FRIEND:
            best = chosen
            return

        for food in can_eat[first]:
            for j in eaters[food]:
                edible[j] += 1

            search(edible, chosen+1)

            for j in eaters[food]:
                edible[j] -= 1

    search(edible, 0)
    return best


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        FRIEND, MEAL = (int(n) for n in input().strip().split())
        friends = list(input().strip().split())
        eaters = [list() for _ in range(MEAL)]

        for food in eaters:
            satisfies = list(input().strip().split())[1:]
            for f in satisfies:
                food.append(friends.index(f))

        ans.append(minimum_foods(eaters, FRIEND))

    for n in ans:
        print(n)
