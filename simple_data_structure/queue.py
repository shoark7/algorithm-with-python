"""Circular Queue in Python

Queue is FIFO(First In, First Out) data structure. It's very famous you know.
Have you seen the movie 'Whiplash'(Damien Chazelle, 2014)?

At the last scene of the movie,
Andrew says to Fletcher, "I'll queue you".
Queue is not far from us. :)


Queue here has these methods:
    is_empty
    is_full
    dequeue
    enqueue


Date: 2018/02/25
"""


class Queue:
    """Circular queue in Python

    It's also called as 'circular buffer'.
    You have to assign its max size when initializing the queue.
    This supports methods like below:
        is_empty: Check if queue is empty
        if_full : Check if queue is full
        enqueue : Append a value to the queue
        dequeue : Pull out the oldest value in the queue
    """
    def __init__(self, max_size=10):
        self._front = 0
        self._rear = 0
        self.__buffer = [0 for _ in range(max_size+1)]
        self._max_size = max_size + 1

    def is_empty(self):
        """Check if the queue is empty"""
        if self._front == self._rear:
            return True
        else:
            return False

    def is_full(self):
        """Check if the queue is full"""
        if (self._front - self._rear) % self._max_size == 1:
            return True
        else:
            return False

    def dequeue(self):
        """Pull out the oldest value in the queue"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        value = self.__buffer[self._front]
        self._front += 1
        self._front %= self._max_size
        return value

    def enqueue(self, value):
        """Put a value to the tip of the queue"""
        if self.is_full():
            raise ValueError("Queue is full")
        self.__buffer[self._rear] = value
        self._rear += 1
        self._rear %= self._max_size
