"""Return if braces in strings are valid or not for each sentence

:input:
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

:return:
yes
yes
no
no
no
yes
yes

URL: https://www.acmicpc.net/problem/4949
ID : 4949
"""
def is_valid_string(strng):
    OPENING = '(['
    CLOSING = ')]'

    opener_stack = []
    for c in strng:
        if c in OPENING:
            opener_stack.append(c)
        elif c in CLOSING:
            if not opener_stack:
                return False
            o = opener_stack.pop()
            if OPENING.index(o) != CLOSING.index(c):
                return False

    return False if opener_stack else True


if __name__ == '__main__':
    while True:
        strng = input()
        if strng == '.':
            break
        else:
            print('yes' if is_valid_string(strng) else 'no')
