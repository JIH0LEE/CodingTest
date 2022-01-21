# 검문
import sys
input = sys.stdin.readline
n = int(input())
inputs = []
result = []
for i in range(n):
    inputs.append(int(input()))
max_value = max(inputs)
for i in range(2, max_value):
    temp = inputs[0] % i
    flag = True
    for elem in inputs:
        if elem % i != temp:
            flag = False
            break
    if flag:
        print(i, end=" ")
