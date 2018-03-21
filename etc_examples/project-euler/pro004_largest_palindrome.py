"""앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?


Date: 2018/03/21
"""


def is_palindrome(n):
    n = str(n)
    length = len(n)
    isit = False
    mid = length // 2

    for i in range(mid):
        if n[i] != n[length-1-i]:
            return False

    return True

max_value = 0


for diff in range(900):
    a, b = 100, 100 + diff
    while b <= 999:
        if is_palindrome(a * b):
            max_value = max_value if max_value > a * b else a * b
        a += 1
        b += 1

print(max_value)
