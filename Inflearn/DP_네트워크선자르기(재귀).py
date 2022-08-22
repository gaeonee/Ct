import sys
import math
#sys.stdin=open("input.txt", "rt")
import heapq
import itertools
import re
from collections import deque #BFS

def dp(n):
    if dy[n] > 0: #������ : �̹� �޸������̼��� �Ǿ������� �ٽ� ��͸� ���������ʰ� �ش簪�� ��ȯ�ϴ°� ������ ����
        return dy[n]
    if n == 1 or n == 2:
        return n
    else:
        dy[n] = dp(n-1) + dp(n-2)
        return dy[n]

n = int(input())
dy = [0] * (n+1)
print(dp(n))