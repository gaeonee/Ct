import sys
from collections import deque


def bfs(p):
	start=[]
	for i in range(5):
		for j in range(5):
		    if p[i][j]=='P':
		        start.append([i,j])

	for s in start:
        queue= deque([s])
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

		while queue:
            x,y=queue.popleft()
            
            dx=[0,0,-1,1]
            dy=[-1,1,0,0]

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0: #좌표가 범위내에 해당되면

                    if p[nx][ny]=='O':
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                        distance[nx][ny]=distance[x][y]+1

                    if p[nx][ny]=='P' and distance[x][y]<=1:
                        return 0
    return 1

def solution(places):
    answer=[]

    for i in places:
        answer.append(bfs(i))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)

'''
https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
응시자의 위치를 start에 추가시킴
start부터 방문하지않은 곳을 방문하면서 다른 응시자를 찾는다
다른응시자를 찾았을때 사이의 위치를 파악한다. 사이거리가 2이하이면 0을 반환
start부터 x가 나오면 가로막힌것이므로 멈춘다
'''