# 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
targets = list(map(int, input().split()))
q = [i+1 for i in range(n)]
dq = deque(q)
count = 0
for target in targets:
    while True:
        if dq[0] == target:
            dq.popleft()
            break
        else:
            if dq.index(target) <= len(dq)/2:
                while dq[0] != target:
                    dq.rotate(-1)
                    count += 1
            else:
                while dq[0] != target:
                    dq.rotate(1)
                    count += 1
print(count)
