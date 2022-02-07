from collections import deque
import sys
n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    op = list(sys.stdin.readline().split())

    if op[0] == 'push_front':
        deq.appendleft(op[1])
    elif op[0] == 'push_back':
        deq.append(op[1])
    elif op[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif op[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif op[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif op[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])
    elif op[0] == 'size':
        print(len(deq))
    elif op[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
