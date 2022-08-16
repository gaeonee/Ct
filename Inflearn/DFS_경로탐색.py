import sys


def dfs(v):
    global cnt #���������� �ƴ� �۷ι� ������ �����ؾ� �Ʒ� cnt�� ������ �� ����
    if v == N:
        cnt += 1
    else:
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)
                visited[i] = 0


N, M= map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

cnt = 0
visited[1] = 1
dfs(1)
print(cnt)
