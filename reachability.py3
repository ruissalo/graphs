import sys

def dfs(adj, x, y):
    visited, stack = set(), [x]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == y:
                return 1
            stack.extend(set(adj[vertex]) - visited)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(dfs(adj, x, y))

