# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    graph.append(input().strip())
visited = [[[0 for i in range(m)] for j in range(n)] for k in range(2)]

visited[0][0][0] = 1
queue = deque([[0, 0, 0]])
flag = False
while queue:
    x, y, z = queue.popleft()

    if x == n-1 and y == m-1:
        print(visited[z][x][y])
        flag = True
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[z][nx][ny] == 0:

            # 벽을 만났을 때,
            if graph[nx][ny] == "1" and z == 0:

                visited[z+1][nx][ny] = visited[z][x][y]+1
                queue.append([nx, ny, z+1])

            elif graph[nx][ny] == "0":

                visited[z][nx][ny] = visited[z][x][y]+1
                queue.append([nx, ny, z])

if not flag:
    print(-1)
