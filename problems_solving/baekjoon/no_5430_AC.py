"""Do AC language calculations over integer array

url: https://www.acmicpc.net/problem/5430
"""
from collections import deque

ERROR_MESSAGE = 'error'
REVERSE, DISCARD = 'RD'


def do_ac_calculations(arr, cmds):
    deck = deque(arr)

    # Preprocess commands
    tmp_r = 0
    new_cmds = ''

    for c in cmds:
        if c == DISCARD:
            new_cmds += REVERSE if tmp_r % 2 else ''
            new_cmds += DISCARD
            tmp_r = 0
        else:
            tmp_r += 1

    new_cmds += REVERSE if tmp_r % 2 else ''


    # Do real calculations
    reverse_now = False
    for c in new_cmds:
        if c == REVERSE:
            reverse_now ^= True
        else:
            if not deck:
                return ERROR_MESSAGE

            if reverse_now:
                deck.pop()
            else:
                deck.popleft()

    if reverse_now:
        deck.reverse()

    return list(deck)


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        cmds = input()
        input()
        arr = eval(input())
        ans.append(do_ac_calculations(arr, cmds))

    for ret in ans:
        ret = str(ret).replace(' ', '')
        print(ret)
