from itertools import combinations

n = [int(input()) for _ in range(9)]

n = list(combinations(n, 7))
for i in range(len(n)):
    if sum(n[i])==100:
        seven = list(n[i])
        seven.sort()
        for i in seven:
            print(i)
        break