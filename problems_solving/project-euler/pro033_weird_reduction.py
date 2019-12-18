# 2. Return whether a fractions number can be reduced in an weird way.
def can_weird_reduce(dividend, divisor):
    dividend, divisor = str(dividend), str(divisor)

    for a in str(dividend):
        for b in str(divisor):
            if a == b and a != '0' and b != '0':
                p1 = int(dividend[1-dividend.index(a)])
                p2 = int(divisor[1-divisor.index(b)])
                if p1 != 0 and int(divisor) / int(dividend) == p2 / p1:
                    return True
    return False


fractions = []

# 1. Combinate over all two digit fractions less than 1.
for a in range(10, 100):
    for b in range(a+1, 100):
        if can_weird_reduce(a, b):
            fractions.append((a, b))

    if len(fractions) == 4:
        break


# 3. Calculate the answer
ans = 1

for a, b in fractions:
    ans *= (b / a)


print(int(ans))
