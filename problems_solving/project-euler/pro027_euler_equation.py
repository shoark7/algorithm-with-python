"""
오일러는 다음과 같은 멋진 2차식을 제시했습니다.

n2 + n + 41
이 식의 n에다 0부터 39 사이의 숫자를 넣으면, 그 결과는 모두 소수가 됩니다.
하지만 n = 40일 때의 값 402 + 40 + 41 은 40×(40 + 1) + 41 이므로 41로 나누어지고, n = 41일 때 역시
412 + 41 + 41 이므로 소수가 아닙니다.

컴퓨터의 발전에 힘입어 n2 − 79n + 1601 이라는 엄청난 2차식이 발견되었는데, 이것은 n이 0에서 79
사이일 때 모두 80개의 소수를 만들어냅니다. 이 식의 계수의 곱은 -79 × 1601 = -126479가 됩니다.

아래와 같은 모양의 2차식이 있다고 가정했을 때,

n2 + an + b   (단 | a | < 1000, | b | < 1000)
0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 2차식을 찾아서, 그 계수 a와 b의 곱을
구하세요.
"""
import time


def is_prime(n):
    if n in [2, 3]:
        return True
    elif n <= 1:
        return False

    for d in range(2, int(n ** (1/2) + 1)):
        if n % d == 0:
            return False
    return True


def euler_equation():
    max_a = 0
    max_b = 0
    count = 0

    for a in range(-999, 999+1):
        for b in range(-999, 999+1):
            tmp_n = 0
            while is_prime(tmp_n**2 + a*tmp_n + b):
                tmp_n += 1
            if count < tmp_n:
                max_a = a
                max_b = b
                count = tmp_n
    return max_a * max_b


c = time.time()
print(euler_equation())
e = time.time()
print(float(e)-float(c))
