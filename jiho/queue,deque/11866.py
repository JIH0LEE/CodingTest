# 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline
result = []
n, k = map(int, input().split())
q = [i+1 for i in range(n)]
queue = deque(q)
while queue:
    queue.rotate(-(k-1))
    result.append(str(queue.popleft()))

print('<'+', '.join(result)+'>')
