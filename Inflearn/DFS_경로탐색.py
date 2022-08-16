import sys


def dfs(v):
    global cnt #지역변수가 아닌 글로벌 변수로 변경해야 아래 cnt를 참조할 수 있음
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
