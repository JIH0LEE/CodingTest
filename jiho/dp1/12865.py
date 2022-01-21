# 평범한 배낭
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0 for j in range(k+1)] for i in range(n+1)]
inputs = []

for i in range(n):
    inputs.append(list(map(int, input().split())))

for i in range(1, n+1):
    [w, v] = inputs[i-1]
    for j in range(1, k+1):
        if j < w:  # 검사하는 짐의 무게가 더 클 때,
            dp[i][j] = dp[i-1][j]  # 이전의 값을 그대로 넣어줌.

        else:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])
