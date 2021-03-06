# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
inputs = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and inputs[i] > inputs[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
