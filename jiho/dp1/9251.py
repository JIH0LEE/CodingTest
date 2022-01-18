# LCS
# dp로 유명한 문제!
import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()
m = len(a)
n = len(b)
dp = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[m][n])
