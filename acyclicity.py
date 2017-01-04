#Uses python3

import sys
import operator

pre_visit = {}
post_visit = {}

clk = 1
visited = set()
stack = set()

def previsit(v):
    global clk
    #if not v in pre_visit:
    pre_visit[v] = clk
    clk += 1

def postvisit(v):
    global clk
    #if not v in post_visit:
    post_visit[v] = clk
    clk += 1

def dfs(graph, start):
    global visited
    global stack
    visited.add(start)
    previsit(start)
    stack.add(start)
    for next in graph[start]:
        if next in stack:
            print(1)
            sys.exit(0)
        if next not in visited:
            dfs(graph, next)
    postvisit(start)
    stack.remove(start)

def connected(adj):
    connected_components = []
    global visited
    for index in range(len(adj)):
        vertex = index
        if vertex not in visited:
            visited.add(vertex)
            dfs(adj, vertex)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    connected(adj)
    print(0)