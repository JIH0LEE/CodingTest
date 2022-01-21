# 동전 0
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [0 for i in range(n)]
count = 0
for i in range(n):
    coins[i] = int(input())
for j in range(n-1, -1, -1):
    count += k//coins[j]
    k = k % coins[j]

print(count)
