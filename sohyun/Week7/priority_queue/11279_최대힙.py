import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num >= 1:
        heapq.heappush(heap, (-num, num))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])