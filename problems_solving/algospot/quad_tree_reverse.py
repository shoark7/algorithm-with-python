"""Turn an image upside-down and change it into a string


'B' means a sector is all black and 'W' means a sector is all white.
If it is 'X', it means at least one of 4 parts of the image has black and white together.

So when I get the original compressed string of the image,
I have to return a string of the turned out image.

https://algospot.com/judge/problem/read/QUADTREE
"""
def decompress(compressed_img: list, pointer: int, y: int, x: int, size: int):
    char = compressed_img[pointer]
    pointer += 1
    if char == 'b' or char == 'w':
        for dy in range(size):
            for dx in range(size):
                image_board[y+dy][x+dx] = char
    else:
        half = size // 2
        decompress(compressed_img, pointer, y, x, half)
        decompress(compressed_img, pointer, y, x+half, half)
        decompress(compressed_img, pointer, y+half, x, half)
        decompress(compressed_img, pointer, y+half, x+half, half)


def reverse_compressed_img(compressed_img):
    point = 0
    def _reverse():
        nonlocal point
        head = compressed_img[point]
        point += 1
        if head == 'w' or head == 'b':
            return head
        upper_left = _reverse()
        upper_right = _reverse()
        lower_left = _reverse()
        lower_right = _reverse()

        return 'x' + lower_left + lower_right + upper_left + upper_right

    return _reverse()


if __name__ == '__main__':
    tests = ['w', 'xbwwb', 'xbwxwbbwb', 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb']
    for test in tests:
        print(reverse_compressed_img(test))
