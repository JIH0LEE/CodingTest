# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    is_target = [False for i in range(n)]
    is_target[m] = True
    priority = deque(q)
    target = deque(is_target)
    count = 0
    while priority:

        if priority[0] == max(priority):

            count += 1
            if target[0]:
                print(count)
                break
            target.popleft()
            priority.popleft()

        else:
            target.rotate(-1)
            priority.rotate(-1)
