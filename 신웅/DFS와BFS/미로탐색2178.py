from collections import deque
import sys

def bfs(x, y):
    global N, M
    queue = deque([(x,y)])
    while(queue):
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if(nx <= -1 or ny <= -1 or nx >= N or ny >= M):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[temp[0]][temp[1]] + 1
                queue.append((nx,ny))

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)

print(graph[N-1][M-1])