def dfs(x,y):
    if x<= -1 or y <= -1 or x >= M or y >= N:
        return False
    if graph[x][y] == 0:
        return False
    elif graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
        
import sys
T = int(input())
answer = []
for _ in range(T) :
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        a, b = map(int,sys.stdin.readline().split())
        graph[a][b] = 1
    count = 0
    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                count += 1
    answer.append(count)
for i in range(len(answer)):
    print(answer[i])