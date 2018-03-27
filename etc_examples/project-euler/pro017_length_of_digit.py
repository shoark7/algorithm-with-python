"""

1부터 5까지의 숫자를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
    115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.
"""


TABLE = {0: 0, 1: len('one'), 2: len('two'), 3: len('three'), 4: len('four'), 5: len('five'),
         6: len('six'), 7: len('seven'), 8: len('eight'), 9: len('nine'), 10: len('ten'),
         11: len('eleven'), 12: len('twelve'), 13: len('thirteen'), 14: len('fourteen'), 15:
         len('fifteen'),
         16: len('sixteen'), 17: len('seventeen'), 18: len('eighteen'), 19: len('nineteen'), 20:
         len('twenty'),
         30: len('thirty'), 40: len('forty'), 50: len('fifty'), 60: len('sixty'), 70:
         len('seventy'),
         80: len('eighty'), 90: len('ninety'), 'hund': len('hundred'),}


def digit_len(n):
    if n > 999:
        raise ValueError("n Should be an integer UNDER 1000")

    a = n // 100
    bc = n % 100
    b = bc // 10
    c = bc % 10
    r = 0

    if n in TABLE:
        return TABLE[n]
    if a:
        r += (TABLE[a] + TABLE['hund'])
    if a and bc:
        r += len('and')
    if bc in TABLE:
        r += TABLE[bc]
    else:
        r += (TABLE[b*10] + TABLE[c])

    return r


n = 1
s = 0
while n <= 999:
    s += digit_len(n)
    n += 1

s += len('onethousand')
print(s)
