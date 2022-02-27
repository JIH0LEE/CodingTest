def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue :
        start = queue.popleft()
        print(start, end=' ')
        for i in graph[start] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
print()
visited = [False]*(N+1)
bfs(V)