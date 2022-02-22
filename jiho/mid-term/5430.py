# AC
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    ops = input().rstrip()
    n = int(input())
    line = input().rstrip()
    if line == '[]':
        inputs = []
    else:
        inputs = line[1:-1].split(',')

    dq = deque(inputs)
    is_forward = True
    for op in ops:
        if op == 'R':
            is_forward = not is_forward
        else:
            if dq:
                if is_forward:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                dq = 'error'
                break
    if dq == 'error':
        print(dq)
    else:
        if is_forward:
            print('['+','.join(dq)+']')
        else:
            print('['+','.join(reversed(dq))+']')
