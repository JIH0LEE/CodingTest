# 전깃줄
# 어려웠다
import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for i in range(n)]
inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

inputs.sort(key=lambda x: x[0])
for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and inputs[i][1] > inputs[j][1]:
            dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))
