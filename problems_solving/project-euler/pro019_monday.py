"""
다음은 달력에 관한 몇 가지 일반적인 정보입니다.

    * 1900년 1월 1일은 월요일이다.
    * 4월, 6월, 9월, 11월은 30일까지 있고, 1월, 3월, 5월, 7월, 8월, 10월, 12월은 31일까지 있다.
    * 2월은 28일이지만, 윤년에는 29일까지 있다.
    * 윤년은 연도를 4로 나누어 떨어지는 해를 말한다.
    * 하지만 100으로 나누어 떨어지지 않는 해는 윤년이 아니며, 400으로 나누어 떨어지면 윤년이다.

20세기(1901년 1월 1일 ~ 2000년 12월 31일)에서, 매월 1일이 일요일인 경우는 총 몇 번입니까?
"""


WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
CUM_MONTH_DAYS = [sum(MONTH_DAYS[0:i]) for i in range(12)]
CUM_MONTH_DAYS = [d % 7 for d in CUM_MONTH_DAYS]
CUM_MONTH_DAYS.insert(0, 0)
YEAR_DELTA = 365 % 7


def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def weekday(year, month, day):
    total_day = 0

    for y in range(1900, year):
        total_day += YEAR_DELTA if not is_leap(y) else (YEAR_DELTA+1)

    total_day += CUM_MONTH_DAYS[month]
    if is_leap(year) and month >= 3:
        total_day += 1
    total_day += (day - 1)
    total_day %= 7

    return WEEKDAYS[total_day]


count = 0
for year in range(1901, 2000+1):
    for month in range(1, 12+1):
        if weekday(year, month, 1) == 'Sun':
            count += 1

print(count)
