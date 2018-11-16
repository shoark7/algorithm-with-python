"""Get maximum utilities of eating sushi in given budget

:input:
2
6 10000
2500 7
3000 9
4000 10
5000 12
10000 20
15000 1
6 543975612
2500 7
3000 9
4000 10
5000 12
10000 20
15000 1

:return:
28
1631925

ID : SUSHI
url: https://algospot.com/judge/problem/read/SUSHI
"""
def max_utility(budget, prices, prefs):
    budget //= 100
    prices = [p // 100 for p in prices]
    ret = 0
    cache = [0 for _ in range(20000 // 100+1)]
    item_length = len(prices)

    for b in range(1, budget+1):
        cand = 0
        for dish in range(item_length):
            if b >= prices[dish]:
                cand = max(cand, cache[(b-prices[dish]) % 201] + prefs[dish])
        cache[b % 201] = cand
        ret = max(ret, cand)
    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        prices = []
        prefs = []
        N, budget = (int(n) for n in input().split())

        for _ in range(N):
            p, f = (int(n) for n in input().split())
            prices.append(p)
            prefs.append(f)

        ans.append(max_utility(budget, prices, prefs))

    for n in ans:
        print(n)
