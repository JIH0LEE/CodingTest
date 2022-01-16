import sys
input = sys.stdin.readline
dp = []
n = int(input())


for i in range(n):
    dp.append(list(map(int, input().split())))


for i in range(1, n):
    length = len(dp[i])
    for j in range(length):
        if i == 1:
            dp[i][j] += dp[i-1][0]
        else:
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == length-1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
