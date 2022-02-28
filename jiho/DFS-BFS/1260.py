# DFS와 BFS
from os import TMP_MAX
import sys
from collections import deque
input=sys.stdin.readline
graph = dict()
n, m, v = map(int, input().split())
for i in range(n):
    graph[i+1] = set()
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].add(end)
    graph[end].add(start)


def dfs(v):
    stack = [v]
    visited = []
    while stack:
        target = stack.pop()
        if target not in visited:
            visited.append(target)
            temp = list(graph[target]-set(visited))
            temp.sort(reverse=True)
            stack.extend(temp)

    for elem in visited:
        print(elem, end=" ")
    print()


def bfs(v):
    queue = deque([v])
    visited = []
    while queue:
        target = queue.popleft()
        if target not in visited:
            visited.append(target)
            temp = list(graph[target]-set(visited))
            temp.sort()
            queue.extend(temp)

    for elem in visited:
        print(elem, end=" ")
    print()


dfs(v)
bfs(v)