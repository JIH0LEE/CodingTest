# 최단경로
import sys
from heapq import heappop, heappush
INF = 1000000
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
costs = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]


def dijkstra(start):
    costs[start] = 0
    priority_queue = []
    heappush(priority_queue, (0, start))
    while priority_queue:
        w, e = heappop(priority_queue)
        for adj, weight in graph[e]:
            new_weight = w+weight
            if new_weight < costs[adj]:
                costs[adj] = new_weight
                heappush(priority_queue, (new_weight, adj))


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

for i in costs[1:]:
    print(i if i != INF else "INF")
