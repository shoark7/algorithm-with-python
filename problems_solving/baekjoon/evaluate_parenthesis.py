"""Return value of the evaluated parenthesis expression

:input:
(()[[]])([])

:return:
28

url: https://www.acmicpc.net/problem/2504
"""
expression = input()
OPENS = '(['
CLOSES = ')]'

def evaluate(expression):
    stack = []
    total = 0
    flags = [0, 0]

    for i, c in enumerate(expression):
        if c in OPENS:
            stack.append(c)
            flags[OPENS.index(c)] += 1
        else:
            flags[CLOSES.index(c)] -= 1
            if flags[CLOSES.index(c)] < 0:
                return 0

            num = 0
            op = stack.pop()
            while isinstance(op, int):
                num += op
                op = stack.pop()

            if OPENS.index(op) != CLOSES.index(c):
                return 0

            num = num if num else 1
            stack.append(num * (OPENS.index(op)+2))

    while stack:
        popped = stack.pop()
        if not isinstance(popped, int):
            return 0
        total += popped
    return total


print(evaluate(expression))
