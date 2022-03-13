# 부분합
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
start = 1
end = 1
result = 1000001
sum_dp = [0]
for i in range(1, n+1):
    sum_dp.append(sum_dp[i-1]+arr[i-1])
while True:
    if sum_dp[end]-sum_dp[start-1] >= s:
        result = min(result, end-start+1)
        start += 1
    else:
        end += 1
        if end == n+1:
            break

if result == 1000001:
    print(0)
else:
    print(result)
