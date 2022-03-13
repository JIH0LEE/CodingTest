# 소수의 연속합
import sys
input = sys.stdin.readline
n = int(input())
is_prime = [True for _ in range(n+1)]
prime_num = []
sum_dp = [0]
for i in range(2, n+1):
    if is_prime[i]:
        q = 2
        while q*i <= n:
            is_prime[q*i] = False
            q += 1
for i in range(2, n+1):
    if is_prime[i]:
        prime_num.append(i)
length = len(prime_num)
for i in range(1, length+1):
    sum_dp.append(sum_dp[i-1]+prime_num[i-1])
start = 1
end = 1
count = 0
while start <= end:
    temp = sum_dp[end]-sum_dp[start-1]
    if temp >= n:
        if temp == n:
            count += 1
        start += 1
    else:
        end += 1
        if end == length+1:
            break
print(count)
