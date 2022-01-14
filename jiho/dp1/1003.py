# 피보나치 함수
import sys

input = sys.stdin.readline
dp = [[1, 0], [0, 1]]
n = int(input())
for i in range(39):
    dp.append(None)


def solve(n):
    if n == 0 or n == 1:
        return dp[n]
    if dp[n] == None:
        temp1 = solve(n-1)
        temp2 = solve(n-2)
        dp[n] = [temp1[0]+temp2[0], temp1[1]+temp2[1]]
    return dp[n]


for i in range(n):
    k = int(input())
    result = solve(k)
    print(result[0], result[1])
