from sys import stdin

n = int(stdin.readline())
t,p=[],[]
dp = [0 for _ in range(n+1)]

for _ in range(n):
    ti,pi = map(int, stdin.readline().split())
    t.append(ti)
    p.append(pi)

m=0
for i in range(n):
    m=max(m, dp[i])
    if i+t[i]>n:
        continue
    dp[i+t[i]]=max(m+p[i],dp[i+t[i]])

print(max(dp))
