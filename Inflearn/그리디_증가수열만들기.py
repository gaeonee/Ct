import sys
sys.stdin=open("input.txt", "rt")


N = int(input())
num_array = list(map(int, input().split()))
answer = ""
lt = 0
rt = N-1
last = 0
tmp = []
while lt<=rt:
    if num_array[lt] > last:
        tmp.append((num_array[lt], 'L'))
    if num_array[rt] > last:
        tmp.append((num_array[rt], 'R'))
    tmp.sort()
    if not tmp:
        break
    answer += tmp[0][1]
    last = tmp[0][0]
    if tmp[0][1] == 'L':
        lt += 1
    else:
        rt -= 1
    tmp.clear()
    

print(len(answer))
print(answer)

