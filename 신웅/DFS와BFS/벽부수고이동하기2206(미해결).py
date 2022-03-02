import sys
from collections import deque

def bfs():
    global N, M
    queue = deque([(0,0,False)])
    while queue:
        temp = queue.popleft()
        for i in range(4):
            ny = temp[0] + dy[i]
            nx = temp[1] + dx[i]
            if nx <= -1 or ny <= -1 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 0:
                queue.append((ny,nx,temp[2]))
                graph[ny][nx] = graph[temp[0]][temp[1]] + 1
            elif graph[ny][nx] == 1:
                if temp[2] == True:
                    continue
                else:
                    queue.append((ny,nx,True))
                    graph[ny][nx] = graph[temp[0]][temp[1]] + 1

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,input()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
bfs()
if N == 1 and M == 1:
    print(1)
elif graph[N-1][M-1] == 0:
    print(-1)
else:
    print(graph[N-1][M-1] + 1)