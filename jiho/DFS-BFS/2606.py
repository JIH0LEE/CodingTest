# 바이러스
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = dict()
for i in range(n):
    graph[i+1] = set()
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)
queue = deque([1])
visited = []
while queue:
    target = queue.popleft()
    if target not in visited:
        visited.append(target)
        temp = list(graph[target]-set(visited))
        temp.sort()
        queue.extend(temp)
print(len(visited)-1)
