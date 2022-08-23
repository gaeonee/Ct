def dfs(L, S, T):
    global res
    if T > m:
        return
    if L == n:
        if S > res:
            res = S
    else:
        dfs(L+1, S + pv[L], T + pt[L])
        dfs(L+1, S, T)


n, m = map(int,input().split())
pv = list() #점수리스트
pt = list() #시간리스트
for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)

res = -1232793821
dfs(0, 0, 0)
print(res)