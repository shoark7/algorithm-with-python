"""
피보나치 수열은 아래와 같은 점화식으로 정의됩니다.

Fn = Fn-1 + Fn-2  (단, F1 = 1, F2 = 1).
이에 따라 수열을 12번째 항까지 차례대로 계산하면 다음과 같습니다.

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
수열의 값은 F12에서 처음으로 3자리가 됩니다.

피보나치 수열에서 값이 처음으로 1000자리가 되는 것은 몇번째 항입니까?
"""
def d(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count


def fibo_nth(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a


n = 1
while True:
    if d(fibo_nth(n)) >= 1000:
        print(n)
        break
    n += 1
