# 1. 고전적인 Trie 선언. 영어 소문자만 사용한다고 가정
ALPHA_LENGTH = 26

def to_number(char):
    return ord(char) - ord('a')


class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHA_LENGTH
        self.terminal = False

    def insert(self, word, idx=0):
        if idx == len(word):
            self.terminal = True
        else:
            char = word[idx]
            char_num = to_number(char)
            if self.children[char_num] is None:
                self.children[char_num] = TrieNode()
            node = self.children[char_num]
            node.insert(word, idx+1)

    def find(self, word, idx=0):
        if idx == len(word):
            return self.terminal
        else:
            char = word[idx]
            char_num = to_number(char)
            if self.children[char_num] is None:
                return False
            else:
                node = self.children[char_num]
                return node.find(word, idx+1)


# 2. 나만의 방식. children을 "char: node" 형태로 표현
class TrieNode:
    def __init__(self, is_root=False):
        self.children = {}
        self.terminal = False
        self.is_root = is_root

    def insert(self, word, idx=0):
        if len(word) == idx:
            self.terminal = True
        else:
            char = word[idx]
            if char not in self.children:
                self.children[char] = TrieNode()

            node = self.children[char]
            node.insert(word, idx+1)


    def find(self, word, idx=0):
        if idx == len(word):
            return self.terminal
        else:
            char = word[idx]
            if char not in self.children:
                return False
            else:
                node = self.children[char]
                return node.find(word, idx+1)
