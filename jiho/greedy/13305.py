# 주유소

import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price=price[0]
result = 0
for i in range(n-1):
    if price[i]<min_price:
        min_price=price[i]
    result+=min_price*cost[i]

print(result)
