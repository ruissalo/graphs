#Uses python3

import sys
import queue
import itertools
from collections import deque

def distance(adj, s, t):

    flatten = list(itertools.chain.from_iterable(adj))
    dist = {x: None for x in flatten}
    dist[s] = 0
    queue = deque([s,])
    while queue:
        u = queue.popleft()
        for node in adj[u]:
            if dist[node] is None:
                queue.append(node)
                dist[node] = dist[u] + 1
            if node == t:
                return dist[node]
    return -1



    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
