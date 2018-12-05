"""Return number of candidates of possible passwords Jaehoon set

:input:
3
2 2 10
12 486 486
200 1000000 2000000

:return:
4
1
19

url: https://algospot.com/judge/problem/read/PASS486
ID : PASS486
"""
# from my_module import get_execution_time

# Way 1
# @get_execution_time
def cand_n(N, lo, hi):
    ans = 0
    n_factors = [0 for _ in range(hi+1)]
    min_factor = [n for n in range(hi+1)]
    min_power = [0 for _ in range(hi+1)]

    min_factor[0] = min_factor[1] = -1

    for i in range(2, hi+1):
        if min_factor[i] == i:
            for j in range(i*i, hi+1, i):
                if min_factor[j] == j:
                    min_factor[j] = i

    def cnt_factor(n_factors):
        n_factors[1] = 1
        for n in range(2, hi+1):
            # 가장 작은 소인수가 자신이면, 곧 소수.
            # 소수는 승도 1이고, 약수 개수도 2
            if min_factor[n] == n:
                min_power[n] = 1
                n_factors[n] = 2
            # if n is composite number
            else:
                p = min_factor[n]
                m = n // p
                if p != min_factor[m]:
                    min_power[n] = 1
                else:
                    min_power[n] = min_power[m] + 1
                a = min_power[n]
                n_factors[n] = (n_factors[m] // a) * (a + 1)

    cnt_factor(n_factors)

    for n in range(lo, hi+1):
        if n_factors[n] == N:
            ans += 1
    return ans

"""
# way 2.
@get_execution_time
def cand_n(N, lo, hi):
    n_factors = [0 for _ in range(hi+1)]
    ans = 0

    for div in range(1, hi+1):
        for i in range(div, hi+1, div):
            n_factors[i] += 1

    for n in range(lo, hi+1):
        ans += (1 if n_factors[n] == N else 0)
    return ans
"""


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, lo, hi = (int(n) for n in input().split())
        ans.append(cand_n(N, lo, hi))

    for n in ans:
        print(n)
