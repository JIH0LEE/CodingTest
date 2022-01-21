# 주유소
# 아마 시간 초과 때문에 58점
import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int, input().split()))
price = list(map(int, input().split()))
final = n
result = 0
while True:
    if final == 0:
        break
    min_price = min(price[:final])
    temp = price.index(min_price)
    result = result + min_price*sum(cost[temp: final])
    final = temp

print(result)
