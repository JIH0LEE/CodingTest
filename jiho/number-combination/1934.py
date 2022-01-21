# 최소공배수
# 최대공약수와 최소공배수
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    min = a if a < b else b
    lcm = 0
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:

            lcm = (a//i)*b
            break
    print(lcm)
