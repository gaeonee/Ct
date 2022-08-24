def dfs(day, money):
    global res
    if day == n:
        if money > res:
            res = money
    else:
        if day + ct[day] <= n:
            dfs(day + ct[day], money + cp[day])
        dfs(day + 1, money)


n = int(input())
ct = list() #점수리스트
cp = list() #시간리스트
for i in range(n):
    a, b = map(int, input().split())
    ct.append(a)
    cp.append(b)

res = -1232793821
dfs(0,0)
print(res)