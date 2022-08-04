def move(L, M, R, n):
	temp = M
	
	if (L+1 == M and M+1 == R):
		return move_list.append(n)
	
	#??-> 중간 ?�동
	if not(M + 1 == R):
		if (M + 1 == R - 1):
			move(temp, M+1, R, n+1)
		else:
			move(temp, M+1, R, n+1)
			move(temp, R-1, R, n+1)
	#??-> ???�동
	if not(M - 1 == L):
		if (M - 1 == L + 1):
			move(L, M-1, M, n+1)
		else:
			move(L, M-1, temp, n+1)
			move(L, L+1, temp, n+1)
	
L, M, R = map(int, input().split())
move_list = []
n = 0
move(L, M, R, n)

print(min(move_list))
print(max(move_list))