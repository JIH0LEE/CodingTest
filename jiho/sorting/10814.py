# 나이순 정렬
import sys
input = sys.stdin.readline

n = int(input())
inputs = []
for i in range(n):
    temp = list(input().split())
    inputs.append(temp)
inputs.sort(key=lambda x: int(x[0]))

for elem in inputs:
    print(elem[0], elem[1])
