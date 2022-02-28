# 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
visited = [[False for i in range(m)] for j in range(n)]
for _ in range(n):
    graph.append(input().strip())
visited[0][0] = True
result = 10000
queue = deque([[0, 0, 1]])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while queue:
    x, y, cnt = queue.popleft()
    if x == n-1 and y == m-1:
        print(cnt)
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if (graph[nx][ny] == "1") and (not visited[nx][ny]):
                queue.append([nx, ny, cnt+1])
                visited[nx][ny] = True
