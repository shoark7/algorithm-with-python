from collections import Counter


MAX_CIRCUMFERENCE = 1000


counter = Counter()

for a in range(1, MAX_CIRCUMFERENCE // 3 + 1):
    for b in range(a+1, MAX_CIRCUMFERENCE // 2 + 1):
        c = (a ** 2 + b ** 2) ** (1 / 2)
        if c.is_integer() and (a + b + c) <= MAX_CIRCUMFERENCE:
            counter[int(a+b+c)] += 1


print(counter.most_common()[0])
