# 큐 2
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])
for i in range(n):
    line = input().split()
    if line[0] == 'push':
        queue.append(line[1])
    elif line[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif line[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
