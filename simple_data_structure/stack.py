"""Simple array-based stack in Python

Stack is FILO or LIFO data structure.
Stack here has methods like below:
    1. push
    2. pop
    3. is_empty
    4. is_full

Date: 2018/02/24
"""


class Stack:
    """Array-based stack in Python

    It has max_size variable that defaults to 10.
    You have to assign it when you initialize the stack.

    It has these kinds of methods:
        is_empty: Check if stack is empty
        is_full : Check if stack is full
        push    : Push a value into a stack
        pop     : PUll out the top element
    """
    def __init__(self, max_size=10):
        self._max_size = max_size
        self._top = 0
        self.__body = [0 for _ in range(self._max_size)]

    def is_empty(self):
        """Check if stack is empty.

        Returns True if stack is empty.
        Otherwise, it returns False
        """
        if self._top == 0:
            return True
        else:
            return False

    def is_full(self):
        """Check if stack is full.

        Returns True if stack's top equals to stack's max size.
        Otherwise, it returns False
        """
        if self._top == self._max_size:
            return True
        else:
            return False

    def push(self, value):
        """Push a value to the tip of the stack"""
        if self.is_full():
            raise ValueError("Stack is full")
        self.__body[self._top] = value
        self._top += 1

    def pop(self):
        """Pull out the last element in the stack"""
        if self.is_empty():
            raise ValueError("Stack doesn't have any element")
        self._top -= 1
        value = self.__body[self._top]
        return value
