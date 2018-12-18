START = 540


if __name__ == '__main__':
    n = 2
    t = 10
    m = 2
    LAST = START + (n-1) * t
    timetable = ["09:10", "09:09", "08:00"]
# timetable = ["08:00", "08:01", "08:22", "08:03"]
# timetable = ['23:59'] * 10
# timetable = ['00:01'] * 5
    timetable = [int(t[:2])*60 + int(t[3:]) for t in timetable]
    timetable.sort()
    timetable = [t for t in timetable if t <= LAST]

    rest = timetable
    s = START
    for i in range(n-1):
        s = START + i * t
        c = 0
        for r in rest[:m]:
            if r <= s:
                c += 1
        _, rest = rest[:c], rest[c:]
    s = LAST

    if len(rest) < m:
        answer = s
    else:
        answer = rest[-1] - 1

    hour, minute = divmod(answer, 60)
    print(f'{hour:02d}:{minute:02d}')
