"""Return largest number of climbing over the wall

:input:
2
3
5 5 15
5 5 10
5 5 5
8
21 15 20 
15 15 10 
13 12 5 
12 12 3 
19 19 2 
30 24 5 
32 10 7 
32 9 4 

:return:
2
5

url: https://algospot.com/judge/problem/read/FORTRESS
ID : FORTRESS
"""
def do_enclose(root, child, walls):
    me = walls[root]
    you = walls[child]

    return me[2] > you[2] and  \
           (me[2] - you[2]) ** 2 > (me[1] - you[1]) ** 2 + (me[0] - you[0]) ** 2


def is_child(root, child, walls):
    if not do_enclose(root, child, walls):
        return False
    for i in range(len(walls)):
        if i != root and i != child and do_enclose(root, i, walls) and do_enclose(i, child, walls):
            return False
    return True


class Node:
    def __init__(self, root, walls):
        self.num = root
        self.children = []

        for i in range(len(walls)):
            if is_child(root, i, walls):
                self.children.append(i)


def max_climbs(walls):
    # MAX( leaf - leaf or leaf - Root )
    longest = 0

    def find(root):
        nonlocal longest

        node = Node(root, walls)

        # Every Tree node has attribute named 'children' which stores children nodes
        heights = []
        for child in node.children:
            # 루트 아래의 서브 트리들의 높이를 저장한다.
            heights.append(find(child))

        # 자식 노드가 없다는 것은 곧 자신이 잎 노드
        if not heights:
            return 0
        heights.sort()

        # 자식 노드가 둘 이상이면 종단간(잎간) 거리를 구할 수 있다.
        # +2는 서브트리 간 이동시 루트를 거쳐가는 비용.
        if len(heights) >= 2:
            longest = max(longest, 2 + heights[-1] + heights[-2])

        return heights[-1] + 1

    heights = find(0)
    return max(longest, heights)


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        walls = []
        for _ in range(N):
            walls.append([int(n) for n in input().split()])
        ans.append(max_climbs(walls))

    for n in ans:
        print(n)
