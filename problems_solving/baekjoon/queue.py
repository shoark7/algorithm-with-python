"""Implement queue and do some chores

:input:
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

:return:
1
2
2
0
1
2
-1
0
1
-1
0
3

url: https://www.acmicpc.net/problem/10845
"""
class Queue:
    def __init__(self):
        self._queue = []
        self._len = 0

    def push(self, v):
        self._queue.append(v)
        self._len += 1

    def pop(self):
        if self.empty():
            return -1
        self._len -= 1
        return self._queue.pop(0)

    def size(self):
        return self._len

    def empty(self):
        return 1 if self._len == 0 else 0

    def front(self):
        if self.empty():
            return -1
        return self._queue[0]

    def back(self):
        if self.empty():
            return -1
        return self._queue[-1]


if __name__ == '__main__':
    C = int(input())
    ans = []
    queue = Queue()
    for _ in range(C):
        line = input()
        if line == 'front':
            ans.append(queue.front())
        elif line == 'back':
            ans.append(queue.back())
        elif line == 'size':
            ans.append(queue.size())
        elif line == 'empty':
            ans.append(queue.empty())
        elif line == 'pop':
            ans.append(queue.pop())
        else:
            _, num = line.split()
            num = int(num)
            queue.push(num)

    for n in ans:
        print(n)
