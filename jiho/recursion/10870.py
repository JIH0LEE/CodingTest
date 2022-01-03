# 피보나치수 5


dp = [None]*21


def solve(n):

    if dp[n] != None:
        return dp[n]
    if n == 0 or n == 1:
        if dp[n] == None:
            dp[n] = n

    else:
        dp[n] = solve(n-1)+solve(n-2)
    return dp[n]


n = int(input())
print(solve(n))
