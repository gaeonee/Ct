from collections import deque #BFS

N = int(input())
farm = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
sum = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
visited[N//2][N//2] = 1
sum += farm[N//2][N//2]
queue.append((N//2,N//2))
L=0
while True:
    if L == N//2: #L이 끝에 도달하면
        break
    for i in range(len(queue)):
        tmp = queue.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if visited[x][y] == 0:
                sum += farm[x][y]
                visited[x][y] = 1
                queue.append((x,y))
                
    L += 1
print(sum)