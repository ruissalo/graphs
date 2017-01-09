#Uses python3

import sys
import queue
import itertools


def distance(adj, cost, s, t):
    #
    size = len(adj)
    prev = {x: [] for x in range(size)}
    dist = {x: float("inf") for x in range(size)}
    H = {x:float("inf")  for x in range(len(adj))}
    H[s] = 0
    dist[s] = 0
    while H:
        u = min(H, key=H.get)
#        if u == t:
#            return(dist[t])
        del H[u]
        for element in adj[u]:
            ind = adj[u].index(element)
            if dist[element] > dist[u] + cost[u][ind]:
                dist[element] = dist[u] + cost[u][ind]
                H[element] = dist[element]
                prev[element] = [u]
            elif dist[element] == dist[u] + cost[u][ind]:
                prev[element].append(u)
    if dist[t] == float("inf"):
        return(-1)
    return dist[t], prev

def dfs_paths(graph, start, goal):
    graph = {key:set(value) for key,value in graph.items()}
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


if __name__ == '__main__':
    input = sys.stdin.read()
    sys.stdin = open('/dev/tty')
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    metric, paths = distance(adj, cost, s, t)
    print(list(dfs_paths(paths,t,s)))
    print(metric)
