"""
N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L이면서 가장 짧은 연속된 음이 아닌 정수 리스트를
구하는 프로그램을 작성하시오.

만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약
길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.
"""
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def int_series(n, l):
    series = []
    if n % l == 0 and l % 2 == 1:
        series = [n // l] * l
        mid = len(series) // 2
        for i in range(1, mid+1):
            series[mid-i] -= i
            series[mid+i] += i
    elif l % 2 == 0 and l // gcd(n, l) == 2:
        series = [n / l] * l
        mid = len(series) // 2
        for i in range(mid):
            series[mid+i] += (i+0.5)
            series[mid-i-1] -= (0.5+i)
        series = [int(n) for n in series]
    return series if all(n >= 0 for n in series) else 0


if __name__ == '__main__':
    n, l = (int(n) for n in input().split())
    exists = False


    while l <= 100:
        series = int_series(n, l)
        if series:
            exists = True
            break
        else:
            l += 1


    if exists:
        answer = ''
        for n in series:
            answer += str(n) + ' '
        print(answer.rstrip())
    else:
        print(-1)
