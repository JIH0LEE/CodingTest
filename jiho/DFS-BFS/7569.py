# 토마토2
import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = []
queue = deque([])
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for z in range(h):
    temp1 = []
    for x in range(n):
        temp2 = list(map(int, input().split()))
        for y in range(m):
            if temp2[y] == 1:
                queue.append([z, x, y])
        temp1.append(temp2)
    graph.append(temp1)

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graph[nz][nx][ny] == 0:
                queue.append([nz, nx, ny])
                graph[nz][nx][ny] = graph[z][x][y]+1

flag = False
day = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                flag = 1
                break

            if graph[z][x][y] > day:
                day = graph[z][x][y]
if flag:
    print(-1)
else:
    print(day-1)
