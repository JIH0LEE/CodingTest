# 회의실 배정
import sys
input = sys.stdin.readline
n = int(input())
inputs = [None for i in range(n)]
for i in range(n):
    inputs[i] = list(map(int, input().split()))
inputs.sort(key=lambda x: x[0])
inputs.sort(key=lambda x: x[1])
count = 0
final = 0
for elem in inputs:
    start, end = elem
    if start >= final:
        final = end
        count += 1

print(count)
