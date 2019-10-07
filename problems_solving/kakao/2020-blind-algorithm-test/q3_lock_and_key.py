"""2020 카카오 신입 개발자 블라인드 테스트 3: 자물쇠와 열쇠

* 핵심 아이디어:
    1. 무조건 자물쇠의 크기가 키의 크기의 이상이다.
       자물쇠의 크기를 3배로 키우고, 자물쇠를 그 가운데에 두어 범위를 벗어나는 것을 피할 수 있다.
    2. 키를 90도로 최대 4번 돌린다. 따라서 해당 알고리즘을 미리 준비해두면 좋다.


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60059
"""
def rotate_matrix_90(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-r-1] = matrix[r][c]

    return ret


def solution(key, lock):
    K, L = len(key), len(lock)
    padded_lock = [[None] * L * 3 for _ in range(L * 3)]
    holes_count = 0

    for r in range(L):
        for c in range(L):
            padded_lock[L+r][L+c] = lock[r][c]
            if lock[r][c] == 0:
                holes_count += 1

    def does_match_here_well(sr, sc):
        matched_count = 0
        for kr in range(K):
            for kc in range(K):
                if key[kr][kc] == 1 and padded_lock[sr+kr][sc+kc] == 1:
                    return False
                elif key[kr][kc] == 1 and padded_lock[sr+kr][sc+kc] == 0:
                    matched_count += 1

        return matched_count == holes_count


    for _ in range(360 // 90):
        key = rotate_matrix_90(key)

        for sr in range(3 * L - K):
            for sc in range(3 * L - K):  # 's' means 'start' here
                if does_match_here_well(sr, sc):
                    return True

    return False
