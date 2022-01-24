# 검문
# 시간 초과 
import sys
input = sys.stdin.readline
n = int(input())
inputs = []
result = []
for i in range(n):
    inputs.append(int(input()))

inputs.sort()
min1=inputs[0]
min2=inputs[1]
for i in range(2, min2+1):
    temp = min1 % i
    flag = True
    for elem in inputs[1:]:
        if elem % i != temp:
            flag = False
            break
    if flag:
        print(i, end=" ")
