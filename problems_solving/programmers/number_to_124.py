"""Change an integer into format of 124 digit notation

:input:
21

:return:
124


url : https://programmers.co.kr/learn/courses/30/lessons/12899
date: 2019/05/24
"""

def solution(n):
    DIGIT_SET = '124'
    d = 1
    left = n - 1 # 왜 1을 빼는지가 핵심... 어렵다.
    ret = ''

    while 3 ** d <= left:
        left -= 3 ** d
        d += 1

    while d - 1 >= 0:
        index, left = divmod(left, 3 ** (d-1))
        ret += DIGIT_SET[index]
        d -= 1

    return ret
