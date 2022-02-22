# 앱
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum_cost = sum(cost)
dp = [[0 for i in range(sum_cost+1)] for j in range(n+1)]

for i in range(1, n+1):
    mem_size = mem[i-1]
    c = cost[i-1]
    for j in range(sum_cost+1):
        if c > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-c]+mem_size, dp[i-1][j])


for i in range(sum_cost+1):
    if dp[n][i] >= m:
        print(i)
        break
