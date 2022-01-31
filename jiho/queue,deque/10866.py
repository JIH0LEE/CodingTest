# 덱
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])
for i in range(n):
    line = input().split()
    if line[0] == 'push_front':
        queue.appendleft(line[1])
    elif line[0] == 'push_back':
        queue.append(line[1])
    elif line[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == 'pop_back':
        if queue:
            print(queue.pop())
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
