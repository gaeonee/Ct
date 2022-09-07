import sys
sys.setrecursionlimit(10**6)
def dfs(start):
    visited[start] = 1

    for i in tree[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += max(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]

n = int(input())
town = [0] + list(map(int, input().split()))
tree = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
dp = [[0, town[i]] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(max(dp[1][0],dp[1][1]))