# 단어 정렬
import sys
input = sys.stdin.readline
n = int(input())
inputs = []
for i in range(n):
    inputs.append(input().strip())
inputs = set(inputs)
inputs = list(inputs)
inputs.sort()
inputs.sort(key=lambda x: len(x))


for elem in inputs:
    print(elem)
