# 유기농 배추
import sys
input = sys.stdin.readline
t = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    for j in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                graph[i][j] = -1
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[nx][ny] == 1:
                                graph[nx][ny] = -1
                                stack.append((nx, ny))

    print(count)
