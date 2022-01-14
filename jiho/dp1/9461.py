# 파도반 수열
import sys
input = sys.stdin.readline

dp = [0 for i in range(101)]
for i in range(4):
    dp[i] = 1


def solve(n):
    if n < 4:
        return dp[n]
    if dp[n] == 0:
        dp[n] = solve(n-2)+solve(n-3)

    return dp[n]


t = int(input())

for i in range(t):
    n = int(input())
    print(solve(n))
