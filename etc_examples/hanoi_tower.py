"""Hanoi tower algorithm in Python

In computer programming, hanoi tower problem is very famous.
Let's get it done with Python

Date: 2018/03/14
"""

_MOVE_COUNT = 0


def hanoi(n):
    """Hanoi tower algorithm in Python

    This gets only one argument named 'n', which indicates a number of disks.
    It should be an integer over 0.

    It traces disks' movement and print it one by one.
    and last prints its total count of movement.
    """
    if not isinstance(n, int) or n <= 0:
       raise Exception("n should be an interger over 0")
    
    global _MOVE_COUNT

    def move(n, start, to):
        """Move one single disk from given start to dest point"""
        global _MOVE_COUNT

        if n == 0:
            return
        move(n-1, start, 6-start-to)
        print(f'{start} -> {to}')
        _MOVE_COUNT += 1
        move(n-1, 6-start-to, to)

    print(f"\nNumber of disks are {n}\n")
    move(n, 1, 3)
    print(f"\nTotal movement counts are {_MOVE_COUNT}")
    _MOVE_COUNT = 0
