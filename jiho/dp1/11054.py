# 가장 긴 바이토닉 부분 수열
# 11053 두번 쓰면 될 것 같은데
import sys
input = sys.stdin.readline
n = int(input())
inputs = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp2 = [0 for i in range(n)]
dp_sum = []
for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and inputs[i] > inputs[j]:
            dp[i] = dp[j]
    dp[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if dp2[i] < dp2[j] and inputs[i] > inputs[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1
for i in range(n):
    dp_sum.append(dp[i]+dp2[i])


print(max(dp_sum)-1)
