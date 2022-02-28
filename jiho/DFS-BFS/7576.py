# 토마토
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
graph = []
queue = deque([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            queue.append([i, j])
    graph.append(temp)

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y]+1

flag = False
day = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
            break

        if graph[i][j] > day:
            day = graph[i][j]
if flag:
    print(-1)
else:
    print(day-1)
