T = int(input())
m_list = []
for i in range(T):
	N, M = map(int, input().split())
	m_list.append(min((N+M)//12, N//5))
for i in m_list:
	print (i)