"""Return right order of chaining the words

:input:
3
4
dog
god
dragon
need
3
aa
ab
bb
2
ab
cd

:return:
need dog god dragon
aa ab bb
IMPOSSIBLE

url: https://algospot.com/judge/problem/read/WORDCHAIN
ID : WORDCHAIN
"""
def wordchain(words):
    def check_euler(outdegree, indegree):
        plus1, minus1 = 0, 0
        for i in range(26):
            delta = outdegree[i] - indegree[i]
            if delta < -1 or delta > 1:
                return False

            if delta == 1:
                plus1 += 1
            elif delta == -1:
                minus1 += 1

        return (plus1 == 1 and minus1 == 1) or (minus1 == 0 or plus1 == 0)

    def euler_circuit(here, circuit):
        for there in range(26):
            while adj[here][there] > 0:
                adj[here][there] -= 1
                euler_circuit(there, circuit)

        circuit.append(here)

    def get_euler_circuit_or_trail(outdegree, indegree):
        circuit = []
        for i in range(26):
            if outdegree[i] == indegree[i] + 1:
                euler_circuit(i, circuit)
                return circuit

        for i in range(26):
            if outdegree[i]:
                euler_circuit(i, circuit)
                return circuit

        return circuit

    def make_graph(words):
        adj = [[0] * 26 for _ in range(26)]
        graph = [[[] * 26 for _ in range(26)] for _ in range(26)]

        indegree = [0] * 26
        outdegree = [0] * 26

        for w in words:
            s = ord(w[0]) - ord('a')
            e = ord(w[-1]) - ord('a')

            graph[s][e].append(w)
            adj[s][e] += 1
            outdegree[s] += 1
            indegree[e] += 1

        return graph, adj, outdegree, indegree

    graph, adj, outdegree, indegree = make_graph(words)

    if not check_euler(outdegree, indegree):
        return "IMPOSSIBLE"

    circuit = get_euler_circuit_or_trail(outdegree, indegree)

    if len(circuit) != len(words) + 1:
        return "IMPOSSIBLE"

    circuit = circuit[::-1]
    ret = ''

    for i in range(1, len(circuit)):
        a = circuit[i-1]
        b = circuit[i]

        if ret:
            ret += ' '
        ret += graph[a][b].pop()

    return ret


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        words = []
        for _ in range(N):
            words.append(input())

        ans.append(wordchain(words))

    for n in ans:
        print(n)
