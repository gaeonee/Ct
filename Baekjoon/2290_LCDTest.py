s, n = map(int, input().split())

def top(num):
    for i in range(1,s+1):
        num[0][i] = '-'
def lt(num):
    for i in range(1,s+1):
        num[i][0] = '|'
def rt(num):
    for i in range(1,s+1):
        num[i][-1] = '|'
def md(num):
    for i in range(1,s+1):
        num[s+1][i] = '-'
def lb(num):
    for i in range(s+2,s*2+2):
        num[i][0] = '|'
def rb(num):
    for i in range(s+2, s*2+2):
        num[i][-1]='|'
def bt(num):
    for i in range(1,s+1):
        num[s*2+2][i] = '-'

def lcd(c, num):
    if c in [0,2,3,5,6,7,8,9]:
        top(num)
    if c in [0,4,5,6,8,9]:
        lt(num)
    if c in [0,1,2,3,4,7,8,9]:
        rt(num)
    if c in [2,3,4,5,6,8,9]:
        md(num)
    if c in [0,2,6,8]:
        lb(num)
    if c in [0,1,3,4,5,6,7,8,9]:
        rb(num)
    if c in [0,2,3,5,6,8,9]:
        bt(num)

n = str(n)
arr = []

for c in n:
    num = [[' ']*(s+2) for _ in range(s*2+3)]
    lcd(int(c), num)
    arr.append(num)

ans = [[] for _ in range(s*2+3)]


for i in range(s*2+3):
    for idx in range(len(arr)):
        ans[i] += arr[idx][i]
        ans[i].append(' ')

for c_arr in ans:
    print(''.join(c_arr))