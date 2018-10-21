import math
import string


MUL = 2 ** 16


def process_str(str1):
    """Process original string

    This function splits original string into list of substrings.
    1. Split text into a list of sub strings. delimeters are any non-alphabetic characters.
       So all elements in the list is alphabetic.
    2. Make a new list of substrings which is ALPHA and must be 2 lengths looping over the list.

    Also process the str1 as if it is all uppercase.(ignore case)


    ex)
        'abc,x,y,dfs' -> ['ab', 'bc', 'df', 'fs']

    :input:
        str1: original data. Must be STR.
    :return:
        A LIST of sub strings of length 2. EX) ['ab', 'bc', 'df', 'fs']
    """
    str1 = str1.upper()
    words = []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            words.append(str1[i:i+2])
    return words


def caps_cups(str1: list, str2: list):
    """Return the list of intersection and union of str sets together

    This function supposes that all data is preprocessed by process_str.
    With that lists of substrings, this makes two lists:
        Intersections sets -> caps
        Union sets -> cups

    Caps and cups are multisets: allows duplicated elements.

    :input:
        str1, str2: LIST of substrings. ex) ['ab', 'ab', 'ab', 'bc', 'cd', 'df', 'ss']
                    Length of all elements are same: 2.
    :return:
        Two lists: one is a list of intersections and the other is a list of union.
    """
    str1.sort()
    str2.sort()
    i1 = i2 = 0
    len_1 = len(str1)
    len_2 = len(str2)
    caps = []
    cups = []

    while i1 < len_1 or i2 < len_2:
        if i1 < len_1 and i2 < len_2 and str1[i1] == str2[i2]:
            cups.append(str1[i1])
            caps.append(str1[i1])
            i1 += 1
            i2 += 1
        elif i1 < len_1 and (i2 == len_2 or str1[i1] < str2[i2]):
            cups.append(str1[i1])
            i1 += 1
        else:
            cups.append(str2[i2])
            i2 += 1
    return caps, cups


def j(str1, str2):
    """Calculate the Jaccard index between two strings

    When original two strings are given, this function calculates the Jaccard index.
    It takes original strings and process them with process_str and caps_cups functions

    It gets the index by dividing length of caps bby length of cups.

    Range of the index is between 0 and 1(including both ends).
    Also, if two strings are all empty strings, just return 1 because of ZeroDivisionError.
    """
    if not str1 and not str2:
        return 1

    set_1 = process_str(str1)
    set_2 = process_str(str2)
    caps, cups = caps_cups(set_1, set_2)
    return len(caps) / len(cups)


def calculate_answer(str1, str2):
    index = j(str1, str2)
    return math.trunc(j(str1, str2) * MUL)


if __name__ == '__main__':
    str1 = 'aa1+aa2'
    str2 = 'AAAA12'
    print(calculate_answer(str1, str2))
