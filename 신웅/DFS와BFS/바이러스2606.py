def dfs(start):
    visited[start] = True
    global count
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            count += 1

import sys
N = map(int,sys.stdin.readline())
M = map(int,sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
count = 0
dfs(1)

print(count)