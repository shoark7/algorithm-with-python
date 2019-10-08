"""2020 카카오 신입 개발자 블라인드 테스트 4: 가사 검색

* 핵심 아이디어:
    1. 쿼리의 중복이 가능하기 때문에 꼭 쿼리에 대한 memoization을 실시한다.

* 알고리즘 순서:
    1. 완전 탐색: 70점. 효율성 탈락
    2. Trie 자료구조 사용: 100점


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


# 2. Trie 자료구조 이용
class Trie:
    def __init__(self, char=''):
        self.children = {}
        self.count = 0
        self.char = char


def solution(words, queries):
    MAX_SIZE = 10000
    tries = [Trie() for _ in range(MAX_SIZE+1)]
    tries_reversed = [Trie() for _ in range(MAX_SIZE+1)]
    ans = []

    for word_now in words:
        W = len(word_now)
        node = tries[W]
        node_reversed = tries_reversed[W]
        word_reversed = word_now[::-1]

        for word, node in ((word_now, node), (word_reversed, node_reversed)):
            for c in word:
                node.count += 1
                if c in node.children:
                    node = node.children[c]
                else:
                    new_node = Trie(c)
                    node.children[c] = new_node
                    node = new_node


    def count_match(query, wildcard_at_last=False):
        N = len(query)
        node = tries[N] if wildcard_at_last else tries_reversed[N]
        query = query if wildcard_at_last else query[::-1]

        for c in query:
            if c != '?':
                if c not in node.children:
                    return 0
                node = node.children[c]
            else:
                break

        return node.count

    return [count_match(query, wildcard_at_last=query.endswith('?')) for query in queries]
