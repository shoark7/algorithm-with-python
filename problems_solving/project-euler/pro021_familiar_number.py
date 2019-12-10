"""
n의 약수들 중에서 자신을 제외한 것의 합을 d(n)으로 정의했을 때,
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍이라 하고 a와 b를 각각 친화수(우애수)라고 합니다.

예를 들어 220의 약수는 자신을 제외하면 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 이므로 그 합은 d(220)
= 284 입니다.
또 284의 약수는 자신을 제외하면 1, 2, 4, 71, 142 이므로 d(284) = 220 입니다.
따라서 220과 284는 친화쌍이 됩니다.

10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요.
"""
def divisor_sum(n):
    if n == 1:
        return 0

    s = 1

    for d in range(2, int(n ** (1/2))+1):
        if n % d == 0:
            s += d
            s += n // d

            if d == n // d:
                s -= d
    return s


SIZE = 10000
checker = [0] * (SIZE+1)

for n in range(2, SIZE+1):
    friend = divisor_sum(n)
    if not checker[n] and friend != n and divisor_sum(friend) == n:
        checker[n] = 1
        checker[friend] = 1


print(sum(i for i, n in enumerate(checker) if n))
