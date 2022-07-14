import sys

def solution(places):
	answer = []
	start=[]
	for i in range(5):
		for j in range(5):
			if places=[i][j]='P':
				start.append([i,j])

	for s in start:
		queue= deque([s])
		visited=[[0]*5 for i in range(5)]


		while queue:



    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

'''
https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
응시자의 위치를 start에 추가시킴
start부터 방문하지않은 곳을 방문하면서 다른 응시자를 찾는다
다른응시자를 찾았을때 사이의 위치를 파악한다. 사이거리가 2이하이면 0을 반환
start부터 x가 나오면 가로막힌것이므로 멈춘다
'''