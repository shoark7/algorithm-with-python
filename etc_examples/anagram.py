"""Check if two arguments are anagrams

This algorithm is implement in time complexity O(n).

Start Date: 2018/04/11
End   Date: 2018/04/11
"""
from string import ascii_letters as alphabets


def is_anagram(a, b):
    """Check if two arguments are anagrams

    :input:
        a : STR
        b : STR
    :return:
        True if two are anagrams otherwise False
    """
    if len(a) != len(b):
        return False
    check = [0 for _ in range(len(alphabets))]

    for i in range(len(a)):
        check[ alphabets.index(a[i]) ] += 1
        check[ alphabets.index(b[i]) ] -= 1

    return True if all(c == 0 for c in check) else False
