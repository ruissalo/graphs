#Uses python3

import sys
import itertools

seen =[]


def bellman_ford(adj, cost, s=0):
    global seen
    size = len(adj)
    # dist = {x: float("inf") for x in range(size)}
    dist = {x: 0 for x in range(size)}
    dist[s] = 0
    for i in range(size-1):
        for u in range(size):
            for element in adj[u]:
                ind = adj[u].index(element)
                if dist[element] > dist[u] + cost[u][ind]:
                    dist[element] = dist[u] + cost[u][ind]

    for u in range(size):
        for element in adj[u]:
            ind = adj[u].index(element)
            if dist[element] > dist[u] + cost[u][ind]:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
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
    print(bellman_ford(adj, cost))
