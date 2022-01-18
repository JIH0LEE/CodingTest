# 연속합
# 구글링함
import sys

input = sys.stdin.readline

n = int(input())
inputs = list(map(int, input().split()))
dp = [inputs[0]]
for i in range(n-1):
    dp.append(max(dp[i]+inputs[i+1], inputs[i+1]))

print(max(dp))
