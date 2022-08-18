from collections import deque #BFS

maze = [list(map(int,input().split())) for _ in range(7)]
queue = deque()
dis = [[0]*7 for _ in range(7)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
x,y = 0,0
queue.append((0,0))
maze[0][0] = 1

while queue:
    tmp = queue.popleft()
    for j in range(4):
        x = tmp[0] + dx[j]
        y = tmp[1] + dy[j]
        if 0<=x<=6 and 0<=y<=6 and maze[x][y]==0:
            queue.append((x,y))
            maze[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]]+1
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])