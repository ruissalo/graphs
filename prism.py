#Uses python3
import sys
import math

import sys
import queue
import itertools

def create_adj_list(x):
    size = len(x)
    adj = [None] * size
    nodes = [x for x in range(size)]
    for node in range(size):
        element = nodes.copy()
        element.remove(node)
        adj[node] = element
    return adj

def weight(x,y,node1,node2):
    cost = math.sqrt(math.pow((x[node1] - x[node2]),2) + math.pow((y[node1] - y[node2]),2))
    return cost

def distance(adj,x,y):
    #
    size = len(adj)
    parent = {x: [] for x in range(size)}
    dist = {x: float("inf") for x in range(size)}
    H = {x:float("inf")  for x in range(len(adj))}
    H[0] = 0
    dist[0] = 0
    while H:
        u = min(H, key=H.get)
        del H[u]
        for element in adj[u]:
            if (element in H) and (dist[element] > weight(x,y,u,element)):
                dist[element] = weight(x,y,u,element)
                parent[element] = u
                H[element] = dist[element]
    return sum(dist.values())

def minimum_distance(x, y):
    # Create Adj list
    adj = create_adj_list(x)
    return distance(adj,x,y)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))


