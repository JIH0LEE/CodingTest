# 1로 만들기
import sys
input = sys.stdin.readline
n = int(input())
dp = [0]
dp.extend([0 for i in range(n)])


def get_value(k):
    global n
    if k > n:
        return 1000000
    else:
        return dp[k]


for i in range(n-1, 0, -1):
    dp[i] = min(get_value(i*3), get_value(i*2), get_value(i+1))+1

print(dp[1])
