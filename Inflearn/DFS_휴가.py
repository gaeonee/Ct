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
ct = list() #��������Ʈ
cp = list() #�ð�����Ʈ
for i in range(n):
    a, b = map(int, input().split())
    ct.append(a)
    cp.append(b)

res = -1232793821
dfs(0,0)
print(res)