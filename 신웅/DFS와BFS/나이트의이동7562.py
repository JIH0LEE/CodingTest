import sys
from collections import deque

def bfs():
    global start,end
    if start == end:
        return 0
    queue = deque([start])
    while queue:
        temp = queue.popleft()
        for (x,y) in [(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]:
            nx = temp[0] + x
            ny = temp[1] + y
            if nx == end[0] and ny == end[1]:
                return graph[temp[0]][temp[1]] + 1
            if nx <= -1 or ny <= -1 or nx >= I or ny>= I:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[temp[0]][temp[1]] + 1
                queue.append((nx,ny))

T = int(input())
result = []
for _ in range(T):
    I = int(input())
    graph = [[0]*I for _ in range(I)]
    start = tuple(map(int,sys.stdin.readline().split()))
    end = tuple(map(int,sys.stdin.readline().split()))
    result.append(bfs())
for i in range(T):
    print(result[i])