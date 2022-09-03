def dfs(start):
    global cnt
    visited[start] = 1
    for i in computer[start]:
        if visited[i]==0:
            dfs(i)
            cnt += 1

n = int(input())
cn = int(input())
cnt = 0
computer = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(cn):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

dfs(1)
print(cnt)