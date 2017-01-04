#Uses python3

import sys
import operator

pre_visit = {}
post_visit = {}

clk = 1
visited = set()

def previsit(v):
    global clk
    if not v in pre_visit:
        pre_visit[v] = clk
        clk += 1

def postvisit(v):
    global clk
    if not v in post_visit:
        post_visit[v] = clk
        clk += 1

def dfs(graph, start):
    global visited
    visited.add(start)
    previsit(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next)
    postvisit(start)

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
    x = post_visit
    y = []
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    for element in sorted_x:
        y.append(element[0]+1)
    y.reverse()
    for element in y:
        print(element,end=" ")
