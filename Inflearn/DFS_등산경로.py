
def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and n_list[xx][yy] > n_list[x][y] and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                dfs(xx,yy)
                visited[xx][yy] = 0

n = int(input())
n_list = []
visited = [[0]*n for _ in range(n)] #�湮Ȯ��
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_value = 1000000000
max_value = -12321434


for i in range(n):
    tmp = list(map(int,input().split()))
    n_list.append(tmp)
    for j in range(n):
        if min_value > tmp[j]:
            sx = i
            sy = j
            min_value = tmp[j]
        if max_value < tmp[j]:
            ex = i
            ey = j
            max_value = tmp[j]

cnt = 0
visited[sx][sy] = 1
dfs(sx, sy)
print(cnt)
