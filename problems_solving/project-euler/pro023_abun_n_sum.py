"""
자신을 제외한 약수(진약수)를 모두 더하면 자기 자신이 되는 수를 완전수라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수, 자신보다 클 때는 초과수라고 합니다.

12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 초과수 중에서는 가장 작습니다.
따라서 초과수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 초과수의 합으로 표현 가능함을 보일 수가
있습니다.
두 초과수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는
더 이상 이 한계값을 낮출 수 없다고 합니다.

그렇다면, 초과수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?
"""
import time


start = time.time()
checker = [1 for _ in range(28123*2+1)]
abun_list = []


def is_abundant(n):
    s = 1
    inted_sqrt = int(n**(1/2))
    for d in range(2, inted_sqrt+1):
        if n % d == 0:
            s += d
            s += n // d
    if inted_sqrt ** 2 == n:
        s -= inted_sqrt

    return True if s > n else False


n = 2
while n <= 28123:
    if is_abundant(n):
        abun_list.append(n)
    n += 1


length = len(abun_list)
for i in range(length):
    for j in range(i, length):
        checker[abun_list[i] + abun_list[j]] = 0


s = 0
for i, n in enumerate(checker[:28123+1]):
    if n:
        s += i

print(s)
end = time.time()
print(end - start)
