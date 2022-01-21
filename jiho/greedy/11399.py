# ATM
import sys
input = sys.stdin.readline
n = int(input())
inputs = list(map(int, input().split()))
inputs.sort()
result = 0
for i in range(n):
    result += inputs[i]*(n-i)
print(result)
