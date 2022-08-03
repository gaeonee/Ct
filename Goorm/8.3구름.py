goorm_array = [list(input()) for _ in range(10)]
H_idx = [[x, y] for x in range(10) for y in range(10) if goorm_array[x][y]=='H'] #H?„ì¹˜
R_idx = [[x, y] for x in range(10) for y in range(10) if goorm_array[x][y]=='R'] #R?„ì¹˜
M_idx = [[x, y] for x in range(10) for y in range(10) if goorm_array[x][y]=='M'] #M?„ì¹˜

distance = (abs(H_idx[0][0] - M_idx[0][0]) + abs(H_idx[0][1] - M_idx[0][1]))-1

if(H_idx[0][0] == R_idx[0][0] == M_idx[0][0] or H_idx[0][1] == R_idx[0][1] == M_idx[0][1]):
	distance += 2
	
print (distance)