# 포도주 시식
import sys
input = sys.stdin.readline
n = int(input())

cost = []
for i in range(n):
    cost.append(int(input()))
dp = [cost[0]]
for i in range(1, n):
    if i == 1:
        dp.append(dp[0]+cost[i])
    elif i == 2:
        dp.append(sum(cost[0:3])-min(cost[0:3]))
    else:
        dp.append(max(dp[i-1], dp[i-2]+cost[i], dp[i-3]+cost[i-1]+cost[i]))


print(dp[n-1])
