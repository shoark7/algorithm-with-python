"""Get minimum number of moves to locate unit to destination

url: https://www.acmicpc.net/problem/2194
"""
from collections import deque
import sys

input = sys.stdin.readline


def get_least_moves(SIZE_R, SIZE_C, R, C, START, END, blocks):
    DELTAS = {'EAST': (0, 1), 'WEST': (0, -1), 'NORTH': (-1, 0), 'SOUTH': (1, 0)}
    CANNOT_REACH = -1

    queue = deque([START])
    visited = [[False] * SIZE_C for _ in range(SIZE_R)]
    visited[START[0]][START[1]] = True
    blocks_graph = [[0] * SIZE_C for _ in range(SIZE_R)]

    for r, c in blocks:
        blocks_graph[r][c] = 1

    moves = 1

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for direction, (dr, dc) in DELTAS.items():
                new_r, new_c = r + dr, c + dc
                if not (new_r >= 0 and new_r + R - 1 < SIZE_R \
                        and new_c >= 0 and new_c + C - 1 < SIZE_C):
                    continue
                elif visited[new_r][new_c]:
                    continue

                can_go_on = True

                if direction == 'NORTH':
                    for sc in range(C):
                        if blocks_graph[new_r][new_c+sc]:
                            can_go_on = False
                            break
                elif direction == 'SOUTH':
                    for sc in range(C):
                        if blocks_graph[new_r+R-1][new_c+sc]:
                            can_go_on = False
                            break
                elif direction == 'EAST':
                    for sr in range(R):
                        if blocks_graph[new_r+sr][new_c+C-1]:
                            can_go_on = False
                            break
                elif direction == 'WEST':
                    for sr in range(R):
                        if blocks_graph[new_r+sr][new_c]:
                            can_go_on = False
                            break

                if can_go_on:
                    if (new_r, new_c) == END:
                        return moves
                    visited[new_r][new_c] = True
                    queue.append((new_r, new_c))

        moves += 1

    return CANNOT_REACH


if __name__ == '__main__':
    SIZE_R, SIZE_C, R, C, K = (int(n) for n in input().strip().split())
    blocks = []

    for _ in range(K):
        blocks.append(tuple(int(n)-1 for n in input().strip().split()))

    START = tuple(int(n)-1 for n in input().strip().split())
    END = tuple(int(n)-1 for n in input().strip().split())

    print(get_least_moves(SIZE_R, SIZE_C, R, C, START, END, blocks))
