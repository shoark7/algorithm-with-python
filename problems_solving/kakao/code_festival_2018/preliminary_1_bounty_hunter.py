"""Get sum of expected bounties

:input:
6
8 4
13 19
8 10
18 18
8 25
13 16

:return:
1780000
620000
1140000
420000
820000
620000

url: https://www.acmicpc.net/problem/15953
"""
first_price = [5000000, 3000000, 2000000, 500000, 300000, 100000, 0]
first_winner = [1, 2, 3, 4, 5, 6, 79]
n_first = len(first_winner)
p_first_winner = [0 for _ in range(n_first)]

p_first_winner[0] = first_winner[0]
for i in range(1, len(first_winner)):
    p_first_winner[i] = p_first_winner[i-1] + first_winner[i]


second_price = [5120000, 2560000, 1280000, 640000, 320000, 0]
second_winner = [1, 2, 4, 8, 16, 33]
n_second = len(second_winner)
p_second_winner = [0 for _ in range(n_second)]

p_second_winner[0] = second_winner[0]
for i in range(1, len(second_winner)):
    p_second_winner[i] = p_second_winner[i-1] + second_winner[i]


def first_bounty(nth):
    if nth == 0:
        return 0
    for i in range(n_first):
        if nth <= p_first_winner[i]:
            return first_price[i]

def second_bounty(nth):
    if nth == 0:
        return 0
    for i in range(n_second):
        if nth <= p_second_winner[i]:
            return second_price[i]


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        a, b = (int(n) for n in input().split())
        ans.append(first_bounty(a) + second_bounty(b))

    for n in ans:
        print(n)
