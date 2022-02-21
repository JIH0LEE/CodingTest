# 펠린드롬?
import sys
input = sys.stdin.readline
n = int(input())

inputs = list(map(int, input().split()))
m = int(input())
dp = [[0 for i in range(n)] for j in range(n)]
for gap in range(n):
    for start in range(n):
        end = start+gap
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start+1 == end:
            if inputs[start] == inputs[end]:
                dp[start][end] = 1
                continue
        if inputs[start] == inputs[end] and dp[start+1][end-1]:
            dp[start][end] = 1

for i in range(m):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])
