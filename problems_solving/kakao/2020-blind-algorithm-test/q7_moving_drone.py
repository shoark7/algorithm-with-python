"""2020 카카오 신입 개발자 블라인드 테스트 7: 블록 이동하기

* 핵심 아이디어:
    1. '데이터가 프로그램의 구조를 결정한다' -> 드론의 현재 위치 상태를 어떻게 표현하는지가 중요.
       여기서는 풀이에서 제시하는 간단한 형식을 차용함. 단순한 게 최선이다.
    2. 드론이 한 번에 만들어낼 수 있는 다음 위치 후보는 8가지(단순이동 4개, 회전 4개)다.
       이 구현이 중요. 여기서 헤맸다.


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60063
"""
from collections import deque


def solution(board):
    SIZE = len(board)
    ROW_WISE, COLUMN_WISE = range(2)
    OPEN, WALL = range(2)
    START = (0, 0, ROW_WISE)
    END_POINT = (SIZE-1, SIZE-1)
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    queue = deque([START])
    visited = set()
    visited.add(START)
    moves_count = 0

    def _is_in_range(r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE

    def _is_open(r, c):
        return board[r][c] == OPEN

    def _is_ok(r, c):
        return _is_in_range(r, c) and _is_open(r, c)

    def _yield_moves_rowwise(r, c):
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r, new_c+1):
                yield (new_r, new_c, ROW_WISE)

        if _is_ok(r+1, c) and _is_ok(r+1, c+1):
            yield (r, c, COLUMN_WISE)
            yield (r, c+1, COLUMN_WISE)
        if _is_ok(r-1, c) and _is_ok(r-1, c+1):
            yield (r-1, c, COLUMN_WISE)
            yield (r-1, c+1, COLUMN_WISE)

    def _yield_moves_columnwise(r, c):
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r+1, new_c):
                yield (new_r, new_c, COLUMN_WISE)

        if _is_ok(r, c-1) and _is_ok(r+1, c-1):
            yield (r, c-1, ROW_WISE)
            yield (r+1, c-1, ROW_WISE)
        if _is_ok(r, c+1) and _is_ok(r+1, c+1):
            yield (r, c, ROW_WISE)
            yield (r+1, c, ROW_WISE)


    while queue:
        moves_count += 1

        for _ in range(len(queue)):
            r, c, direction = queue.popleft()
            yield_func = _yield_moves_rowwise if direction == ROW_WISE else _yield_moves_columnwise

            for new_coord in yield_func(r, c):
                if new_coord not in visited:
                    queue.append(new_coord)
                    visited.add(new_coord)

                    r, c, direction = new_coord
                    if (r, c+1) == END_POINT or (r+1, c) == END_POINT:
                        return moves_count
