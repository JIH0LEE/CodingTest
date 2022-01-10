# 수 정렬하기 -3
# counting 정렬

import sys
input = sys.stdin.readline

result = [0]*10001

n = int(input())

for i in range(n):
    num = int(input())
    result[num] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)
