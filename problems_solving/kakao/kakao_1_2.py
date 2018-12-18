"""Kakaotal 1차 코딩 테스트 2번 문제

http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
"""
SQUARES = 'SDT'
OPTIONS = '*#'
text = '1S*2T*3S'
n_i = 0
numbers = []
n_now = None


for i in range(len(text)):
    n_c = text[i]
    if n_c.isnumeric():
        if n_now:
            numbers.append(n_now)
            n_i += 1
        if text[i:i+2].isnumeric():
            n_now = int(text[i:i+2])
            i += 1
        else:
            n_now = int(n_c)
    elif n_c in SQUARES:
        if n_c == 'D':
            n_now **= 2
        elif n_c == 'T':
            n_now **= 3
    else:
        if n_c == '*':
            n_now *= 2
            if n_i != 0:
                numbers[n_i-1] *= 2
        else:
            n_now = -n_now
numbers.append(n_now)


print(sum(numbers))
