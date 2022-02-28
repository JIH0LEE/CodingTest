import sys
from collections import deque

def bfs():
    global M, N, H
    while(queue):
        h, n, m = queue.popleft()
        for i in range(6):
            nn = n + dn[i]
            nm = m + dm[i]
            nh = h + dh[i]
            if(nn <= -1 or nm <= -1 or nh <= -1 or nn >= N \
                or nm >= M or nh >= H):
                continue
            if graph[nh][nn][nm] == 0:
                queue.append((nh,nn,nm))
                graph[nh][nn][nm] = graph[h][n][m] + 1

M, N, H = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(N)] for _ in range(H)]
queue = deque([])
for i in range(H):
    for j in range(N):
        graph[i][j] = list(map(int,sys.stdin.readline().split()))
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
dn = [-1,1,0,0,0,0]
dm = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

bfs()
result = 0
breaker1 = False
breaker2 = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                result = -1
                breaker1 = True
                breaker2 = True
                break
            result = max(result, graph[i][j][k])
        if breaker1 == True:
            break
    if breaker2 == True:
        break
if result == -1 :
    print(result)
else:
    print(result - 1)