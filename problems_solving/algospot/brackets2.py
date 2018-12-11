"""Return if brackets match correctly or not

:input
3
()()
({[}])
({}[(){}])

:return:
YES
NO
YES

https://algospot.com/judge/problem/read/BRACKETS2
"""
OPENS = ['(', '{', '[']
CLOSES = [')', '}', ']']


class Stack:
    def __init__(self, arr=[]):
        self._stack = list(arr)
        self._len = len(self._stack)

    def pop(self):
        if self._len == 0:
            raise ValueError("Stack is empty")

        v = self._stack.pop()
        self._len -= 1
        return v

    def push(self, v):
        self._stack.append(v)
        self._len += 1

    def is_empty(self):
        return self._len == 0


def match(string):
    checker = Stack()

    for br in string:
        if br in OPENS:
            checker.push(br)
        else:
            if checker.is_empty():
                return False
            oppo = checker.pop()
            if OPENS.index(oppo) != CLOSES.index(br):
                return False

    return checker.is_empty()


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        sample = input()
        ans.append(match(sample))

    for n in ans:
        print('YES' if n == True else 'NO')
