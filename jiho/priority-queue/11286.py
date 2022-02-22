# 절대값 힙
import sys
import heapq
input=sys.stdin.readline
heap=[]
n=int(input())
result=[]

for i in range(n):
    x=int(input())
    if not x:
        if not heap:
            result.append(0)
        else:
            a=heapq.heappop(heap)
            result.append(a[1])
    else:
        heapq.heappush(heap,(abs(x),x))

for elem in result:
    print(elem)
