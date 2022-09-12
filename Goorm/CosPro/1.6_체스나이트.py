def solution(pos):
	answer = 0
	#chess = [[0 for i in range(8)] for j in range(8)]
	dic={'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
	dx = [-2,-1,1,2,-2,-1,1,2]
	dy = [1,2,2,1,-1,-2,-2,-1]
	x = abs(int(pos[1])-8)
	y = dic[pos[0]]
	for i in range(8):
		if 0 <= x + dx[i] < 8 and 0 <= y+dy[i] < 8:
			answer += 1
	
	return answer