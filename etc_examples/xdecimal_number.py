"""Change given number to target decimal number algorithm

Start Date : 2017/12/24
End  Date  : 2017/12/24
"""


def xdecimal_number(number, x_dec=2):
    """Return x_dec decimal number with given 10 decimal number

    :input:
        number: Wanted 10 decimal number. Should be an int over -1.
        x_dec: Target decimal. Must be an int over 1. Defaults to 2.
    :return:
        str. x_dec decimal number.
    """
    # Input validation
    if not isinstance(number, int) or number <= -1:
        raise ValueError("number must be an integer over -1")
    if not isinstance(x_dec, int) or number <= 1:
        raise ValueError("x_dec must be an integer over 1")

    e = 1
    answer = ''
    while number >= x_dec ** e:
        e += 1
    e -= 1

    for _ in range(e, -1, -1):
        quotient = number // x_dec ** e
        number -= quotient * x_dec ** e
        answer += str(quotient)
        e -= 1

    return answer
