#가운데를 말해요
import sys
import heapq
input=sys.stdin.readline
n=int(input())
small=[]
big=[]
rt=[]
for _ in range(n):
    num=int(input())
    if len(small)==len(big):
        heapq.heappush(small,(-num,num))
    else:
        heapq.heappush(big,(num,num))
    
    if (small and big) and small[0][1]>big[0][1]:
        small_num=heapq.heappop(small)[1]
        big_num=heapq.heappop(big)[1]
        heapq.heappush(small,(-big_num,big_num))
        heapq.heappush(big,(small_num,small_num))

    rt.append(small[0][1])

for elem in rt:
    print(elem)