# 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
for _ in range(t):
    n = int(input())
    visited = [[0 for i in range(n)] for j in range(n)]

    start = list(map(int, input().split()))
    visited[start[0]][start[1]] = 1
    end = list(map(int, input().split()))
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:

            print(visited[x][y]-1)
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]+1
                queue.append([nx, ny])
