# 최대공약수와 최소공배수
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
min = a if a < b else b
gcd = 0
lcm = 0
for i in range(min, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        lcm = (a//i)*b
        break
print(gcd)
print(lcm)
