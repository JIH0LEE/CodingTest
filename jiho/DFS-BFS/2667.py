# 단지 번호 붙이기
import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):

    graph.append(list(map(int, list(input().strip()))))

counts = []
danji = -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            stack = [(i, j)]
            graph[i][j] = danji
            while stack:
                x, y = stack.pop()
                count += 1
                graph[i][j] = danji
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 1:

                            stack.append((nx, ny))
                            graph[nx][ny] = danji
            counts.append(count)
            danji -= 1
counts.sort()
print(len(counts))
for count in counts:
    print(count)
