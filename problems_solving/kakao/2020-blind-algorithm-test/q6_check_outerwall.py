"""2020 카카오 신입 개발자 블라인드 테스트 6: 외벽 점검

* 핵심 아이디어:
    1. 순환하는 외벽 구조는 각 점을 맨 뒤로 이어붙이면서 해결한다.
    2. 필요한 친구 수는 1명부터 D명까지 늘려가되, 각 인원들의 순열도 고려해서 확인한다.


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60062
"""
from itertools import permutations


def solution(N, weak, dist):
    # process data
    dist.sort(reverse=True)
    weak_list = [weak]

    for _ in range(len(weak)-1):
        last = weak_list[-1].copy()
        first = last.pop(0)
        last.append(N + first)
        weak_list.append(last)

    # Solve the problem
    for manpower in range(1, len(dist)+1):
        for tmp_dist in permutations(dist[:manpower], manpower):
            for tmp_weak in weak_list:
                man_idx = 0
                weak_now = weak_idx = 0

                while man_idx < manpower and weak_idx < len(tmp_weak):
                    if tmp_dist[man_idx] >= tmp_weak[weak_idx] - tmp_weak[weak_now]:
                        weak_idx += 1
                    else:
                        weak_now = weak_idx
                        man_idx += 1

                if weak_idx == len(tmp_weak) and man_idx < manpower:
                    return manpower
    return -1
