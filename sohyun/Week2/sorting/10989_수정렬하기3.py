# 카운팅 정렬
import sys
n = int(input())
li = [0 for _ in range(10001)]

for _ in range(n):
    num = int(sys.stdin.readline())
    li[num] += 1

for i in range(1, 10001):
    count = li[i]
    for _ in range(count):
        print(i)