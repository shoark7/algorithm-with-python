"""Get the numbers of white and blue sub-blocks

url: https://www.acmicpc.net/problem/2630
"""
def count_white_blue(board):
    N = len(board)
    WHITE, BLUE = range(2)

    def cut_off(r, c, size):
        color = board[r][c]
        white = blue = 0
        if size == 1:
            return (1, 0) if color == WHITE else (0, 1)
        elif all(board[r+dr][c+dc] == color for dr in range(size) for dc in range(size)):
            return (1, 0) if color == WHITE else (0, 1)

        half_size = size // 2
        for dr in range(2):
            for dc in range(2):
                d_white, d_blue = cut_off(r + dr*half_size, c + dc*half_size, half_size)
                white += d_white
                blue += d_blue
        return white, blue

    return cut_off(0, 0, N)


if __name__ == '__main__':
    N = int(input())
    board = []
    for _ in range(N):
        board.append([int(n) for n in input().split()])

    white, blue = count_white_blue(board)
    print(white)
    print(blue)
