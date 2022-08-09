from sys import stdin
from itertools import combinations

n = int(input())
num = 0

if n % 5 == 0:
    print(n//5)

else:
    while n > 0:
        n -= 3
        num += 1

        if n%5 == 0:
            print(num + n//5)
            break
        elif n == 0:
            print(num)
            break
        elif 3 > n:
            print(-1)
            break