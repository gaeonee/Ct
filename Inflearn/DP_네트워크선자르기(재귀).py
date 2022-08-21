import sys
import math
#sys.stdin=open("input.txt", "rt")
import heapq
import itertools
import re
from collections import deque #BFS

def dp(n):
    if dy[n] > 0: #가지컷 : 이미 메모이제이션이 되어있으면 다시 재귀를 수행하지않고 해당값을 반환하는게 수행이 빠름
        return dy[n]
    if n == 1 or n == 2:
        return n
    else:
        dy[n] = dp(n-1) + dp(n-2)
        return dy[n]

n = int(input())
dy = [0] * (n+1)
print(dp(n))