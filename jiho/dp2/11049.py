# 행렬 곱셈 순서
import sys
input = sys.stdin.readline
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
# dp[i][j] : j 부터 i+j 까지의 곱의 최소 연산수
dp = [[0 for _ in range(n)]]
for i in range(1, n):
    new_dp = []
    for j in range(n-i):
        temp = [dp[k][j]+dp[i-k-1][j+k+1]+mat[j][0] *
                mat[j+k][1]*mat[i+j][1] for k in range(0, i)]
        min_value = min(temp)
        new_dp.append(min_value)
    dp.append(new_dp)

print(dp[n-1][0])
