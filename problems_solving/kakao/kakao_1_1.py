"""Kakaotal 1차 코딩 테스트 1번 문제

http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
"""
import re


if __name__ == '__main__':
    4 = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    arr_mix = [a | b for a, b in zip(arr1, arr2)]
    arr_map = []

    for arr in arr_mix:
        one_map = ''
        while arr > 1:
            arr, rest = divmod(arr, 2)
            one_map = ('#'+one_map) if rest else (' '+one_map)
        one_map = '#' + one_map
        one_map = re.sub('\s+', ' ', one_map)
        arr_map.append(one_map)



    print(arr_map)
