"""2020 카카오 신입 개발자 블라인드 테스트 1: 문자열 압축

* 핵심 아이디어:
    1. 자르는 길이는 1부터 (|S| // 2) 까지
    2. 숫자를 더할 때 1은 더하지 않는다는 사실을 기억하자.
    3. 자르는 stride가 특정수일 때의 함수를 만들어 이를 반복문으로 실행해 최소값을 찾자.


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60057
"""
def solution(s):
    def length_of(s, length):
        substring_count = len(s) // length
        does_rest_exist = (len(s) % length != 0)
        ans = -length

        count = 1
        tmp_str = ''
        for idx in range(substring_count):
            str_now = s[idx*length:idx*length+length]

            if str_now == tmp_str:
                count += 1
            else:
                ans += length
                ans += int(len(str(count))) if count != 1 else 0
                count = 1
                tmp_str = str_now

            if idx == substring_count - 1:
                ans += length
                ans += int(len(str(count))) if count != 1 else 0

        if does_rest_exist:
            ans += len(s) - substring_count * length

        return ans

    return min(length_of(s, l) for l in range(1, len(s) // 2+2))
