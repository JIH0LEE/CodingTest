import heapq
import sys

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if (len(left_heap) != 0 and len(right_heap) != 0) and (left_heap[0] * -1 > right_heap[0]):
        left = heapq.heappop(left_heap) * -1
        right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, right * -1)
        heapq.heappush(right_heap, left)


    print(left_heap[0] * -1)