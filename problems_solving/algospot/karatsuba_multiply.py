"""List based multiplications: 1. Base one, 2: Karatsuba

0. Helper functions
    : Helper functions play important roles when calculating both methods
    - _int_to_list:
        - Change INT into a LIST. Reverse the order.
    - _list_to_int:
        - Change LISt into an INT. Reverse the order.
    - _normalize:
        - Normalize each of elements in a list.
    - _list_sum:
        - Takes 2 lists and add each of elements of lists and return one list.
    - list_multiply:
        - Takes 2 list and return multiplication of the lists into one list.


1. Base one
  : This is a basic multiplications we learn in schools.
    Use helper functions and nothing there is special


2. Karatsuba
  : This is a multiplication developed by Karatsuba.
    It's more effective than the basic one.
    This code is hard, so watch your code!
"""
# Helper functions for both multiplications

def _int_to_list(a):
    new_a = []
    while a:
        new_a.append(a % 10)
        a //= 10
    return new_a


def _list_to_int(a):
    length = len(a)
    new_a = 0
    for i, n in enumerate(a):
        new_a += n * (10 ** i)

    return new_a


def _normalize(ret):
    ret.append(0)
    for i in range(len(ret)-1):
        if ret[i] < 0:
            borrow = (abs(ret[i]) + 9) // 10
            ret[i+1] -= borrow
            ret[i] += borrow * 10
        else:
            ret[i+1] += ret[i] // 10
            ret[i] %= 10

    while len(ret) > 1 and ret[-1] == 0:
        ret.pop()


def _list_sum(a, b, to_sum=True):
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("a, b must be list.")
    if len(a) >= len(b):
        for i in range(len(b)):
            a[i] += (b[i] if to_sum else -b[i])
        _normalize(a)
        return a
    else:
        for i in range(len(a)):
            b[i] += (a[i] if to_sum else -a[i])
        _normalize(b)
        return b


def _list_multiply(a, b):
    ret = [0 for _ in range(len(a)+len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            ret[i+j] += a[i] * b[j]
    while len(ret) > 1 and ret[-1] == 0:
        ret.pop()
    _normalize(ret)
    return ret


def multiply(a, b):
    """Multiply two integers."""
    a, b = _int_to_list(a), _int_to_list(b)
    ret = _list_multiply(a, b)
    _normalize(ret)
    ret = _list_to_int(ret)

    return ret



def karatsuba(a, b):
    """Karatsuba multiplication in Python"""
    def _multiply(a, b):
        an, bn = len(a), len(b)
        if an < bn:
            return _multiply(b, a)
        if an == 0 or bn == 0:
            return []
        if an <= 3:
            return _list_multiply(a, b)

        half = an // 2
        a0 = a[:half]
        a1 = a[half:]
        b0 = b[:min(bn, half)]
        b1 = b[min(bn, half):]

        z2 = _multiply(a1, b1)
        z0 = _multiply(a0, b0)

        a = _list_sum(a0, a1)
        b = _list_sum(b0, b1)

        z1 = _multiply(a, b)
        z1 = _list_sum(z1, z0, to_sum=False)
        z1 = _list_sum(z1, z2, to_sum=False)

        z1 = [0] * half + z1
        z2 = [0] * half * 2 + z2
        z2 = _list_sum(z2, z1)
        z2 = _list_sum(z2, z0)

        return z2

    a, b = _int_to_list(a), _int_to_list(b)
    ret = _multiply(a, b)
    _normalize(ret)
    ret = _list_to_int(ret)

    return ret
