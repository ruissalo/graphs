#Uses python3

import sys
import itertools

def dfs(adj, x):
    visited, stack = set(), [x]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(adj[vertex]) - visited)
    return visited

def connected(adj):
    connected_components = []
    visited = set()
    for index in range(len(adj)):
        vertex = index
        if vertex not in visited:
            visited.add(vertex)
            connected_components.append(dfs(adj, vertex))
    comp_list = [list(x) for x in connected_components]
    sorted_comp_list = [x.sort() for x in comp_list]
    comp_list.sort()
    comp = list(k for k, _ in itertools.groupby(comp_list))
    print(len(comp))


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
    connected(adj)
