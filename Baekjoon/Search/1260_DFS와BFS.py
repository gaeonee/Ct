from sys import stdin
from itertools import combinations
from collections import deque

def bfs (graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        nd = queue.popleft()
        print(nd, end = ' ')

        for i in graph[nd]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

def dfs (graph, node, visited):
    print(node, end = ' ')
    visited[node] = True
    for i in (graph[node]):
        if not visited[i]:
            dfs(graph, i, visited)
            visited[i] = True

n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)
