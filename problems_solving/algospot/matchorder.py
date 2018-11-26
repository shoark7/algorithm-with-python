"""Return maximum number of wins

:input:
3
6
3000 2700 2800 2200 2500 1900
2800 2750 2995 1800 2600 2000
3
1 2 3
3 2 1
4
2 3 4 5
1 2 3 4

:return:
5
3
3

url: https://algospot.com/judge/problem/read/MATCHORDER
ID : MATCHORDER
"""
def max_wins(russians, koreans):
    koreans.sort()
    wins = 0
    # 1. 절대 못 이기는 놈이면 제일 약한 애를 매칭시킨다.
    # 2. 그래도 이길 수는 있으면 그 러시안 친구보다 강한 가장 약한 친구들 내보낸다.
    rm_kor = 0
    for i in range(len(russians)):
        if russians[i] > koreans[-1]:
            rm_kor = 0
        else:
            for j in range(len(koreans)):
                if russians[i] <= koreans[j]:
                    wins += 1
                    rm_kor = j
                    break
        koreans.pop(rm_kor)

    return wins



if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        russians = [int(n) for n in input().split()]
        koreans = [int(n) for n in input().split()]
        ans.append(max_wins(russians, koreans))

    for n in ans:
        print(n)
