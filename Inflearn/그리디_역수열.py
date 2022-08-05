import sys
sys.stdin=open("input.txt", "rt")

N = int(input())
n = 0
reverse = list(map(int, input().split()))
list = [[] for i in range(N)]

while n < N:
    idx = reverse[n]
    for i in range(reverse[n]):
        if list[i] < n+1:
            idx += 1
    list[idx] = n+1
    n += 1