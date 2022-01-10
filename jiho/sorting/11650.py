# 좌표 정렬하기
import sys

input = sys.stdin.readline
inputs = []
n = int(input())
for i in range(n):
    axis = list(map(int, input().split()))
    inputs.append(axis)
inputs = sorted(inputs, key=lambda x: (x[0], x[1]))
for elem in inputs:
    print(elem[0], elem[1])
