# 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = dict()
    not_visited = set([i+1 for i in range(v)])
    for i in range(v):
        graph[i+1] = set()
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    count = 0
    print(not_visited)
    while not_visited:
        count += 1
        queue = deque([list(not_visited)[0]])
        print(queue)
        not_visited -= set([list(not_visited)[0]])
        print(not_visited)
        while queue:
            target = queue.popleft()
            queue.extend(list(graph[target] & not_visited))
            not_visited -= graph[target]
        print(not_visited)
    print("answer:", count)
