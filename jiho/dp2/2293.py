# 동전 1
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    coins.append(int(input()))
for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]
print(dp[k])
