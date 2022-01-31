# 카드 2
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = [i+1 for i in range(n)]
queue = deque(q)

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])
