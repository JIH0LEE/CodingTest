# 약수
import sys
input = sys.stdin.readline
n = int(input())
inputs = list(map(int, input().split()))
inputs.sort()
print(inputs[0]*inputs[-1])
