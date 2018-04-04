"""

2 ≤ a ≤ 5 이고 2 ≤ b ≤ 5인 두 정수 a, b로 만들 수 있는 a ^ b의 모든 조합을 구하면 다음과 같습니다.

2^2=4,  2^3=8,   2^4=16,  2^5=32
3^2=9,  3^3=27,  3^4=81,  3^5=243
4^2=16, 4^3=64,  4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125

여기서 중복된 것을 빼고 크기 순으로 나열하면 아래와 같은 15개의 숫자가 됩니다.

4,  8,  9,  16,  25,  27,  32,  64,  81,  125,  243,  256,  625,  1024,  3125

그러면, 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b를 가지고 만들 수 있는 a ^ b는 중복을 제외하면 모두 몇
개입니까?
"""
from pprint import pprint


# def divisor_gen(n):
    # r = []
    # for d in range(n//2, 1, -1):
        # if n % d == 0:
            # r.append(d)
    # return r


# dynamic table initialization
# dt = [[1 for _ in range(101)] for _ in range(101)]
# for i in range(2):
    # dt[i] = [0 for _ in range(101)]
    # for j in range(101):
        # dt[j][i] = 0


# Calculate
# def square_sum(n):
    # dt = [[1 for _ in range(n+1)] for _ in range(n+1)]
    # for i in range(2):
        # dt[i] = [0 for _ in range(n+1)]
        # for j in range(n+1):
            # dt[j][i] = 0

    # for a in range(2, n+1):
        # for b in range(n, 1, -1):
        # for b in range(2, n+1):
            # if dt[a][b]:
                # divisors = divisor_gen(b)
                # for d in divisors:
                    # c = b // d
                    # if a ** c <= n:
                        # dt[a**c][d] = 0
                    # else:
                        # break

    # print(sum(sum(line) for line in dt))
    # return None


# square_sum(100)

dt = []
for a in range(2, 100+1):
    for b in range(2, 100+1):
        if a ** b not in dt:
            dt.append(a**b)

print(len(dt))
