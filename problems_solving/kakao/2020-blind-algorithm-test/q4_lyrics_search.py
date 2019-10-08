"""2020 카카오 신입 개발자 블라인드 테스트 4: 가사 검색

* 핵심 아이디어:
    1. 쿼리의 중복이 가능하기 때문에 꼭 쿼리에 대한 memoization을 실시한다.

* 알고리즘 순서:
    1. 완전 탐색: 효율성 탈락


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60060
"""
# 1. Exhaustive search solution
def solution(words, queries):
    query_dict = {}
    ans = []

    def match_or_not(word, query):
        if len(word) != len(query):
            return False

        wildcard_count = query.count('?')
        if query.startswith('?'):  # 접두사
            return word[wildcard_count:] == query[wildcard_count:]
        else:
            return word[:len(word)-wildcard_count] == query[:len(word)-wildcard_count]

    for query in queries:
        if query in query_dict:
            ans.append(query_dict[query])
            continue

        count = sum(match_or_not(word, query) for word in words)
        ans.append(count)
        query_dict[query] = count

    return ans
