import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0 for _ in range(sum(c)+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(sum(c)+1):
        if c[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            if (dp[i-1][j-c[i-1]] + a[i-1]) > dp[i-1][j]:
                dp[i][j] = dp[i-1][j-c[i-1]] + a[i-1]
            else:
                dp[i][j] = dp[i-1][j]

for i in range(0, sum(c)+1):
    if (m <= dp[n][i]) :
        print(i)
        break
