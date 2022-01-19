n, k = map(int, input().split())
bag = []
# dp = []
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

for i in range(1, n+1):
    wei = bag[i-1][0]
    val = bag[i-1][1]
    for j in range(1, k+1):
        if wei > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val + dp[i-1][j-wei])


print(dp[-1][-1])