"""Kakaotal 1차 코딩 테스트 3번 문제

http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
"""
import time


cities1 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
cities2 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']

if __name__ == '__main__':
    LENGTH = 5
    HIT_TIME = 1
    MISS_TIME = 5
    cache = [' ' for _ in range(LENGTH)]
    tracer = [0 for _ in range(LENGTH)]
    hitted_index = ''
    total_time = 0
    oldest = 0
    next_value = 1


    if not LENGTH:
        print(len(cities3) * MISS_TIME)
    else:
        for city in cities3:
            is_hitted = False
            for i in range(LENGTH):
                if not is_hitted and city == cache[i] :
                    is_hitted = True
                    hitted_index = i
                oldest = i if tracer[i] < tracer[oldest] else oldest
            if is_hitted:
                tracer[hitted_index] += next_value
                next_value += 1
                total_time += 1
            else:
                tracer[oldest] = next_value
                next_value += 1
                cache[oldest] = city
                total_time += 5
        print(total_time)
