# 검문
import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
inputs = []
for i in range(n):
    inputs.append(int(input()))
result = inputs[1]-inputs[0]
outputs = set()
for i in range(2, n):
    result = gcd(result, abs(inputs[i]-inputs[i-1]))
for i in range(1, int(round(result**0.5))+1):
    if result % i == 0:

        outputs.add(i)
        outputs.add(result//i)

new = list(outputs)
new.sort()
for elem in new[1:]:
    print(elem, end=" ")
