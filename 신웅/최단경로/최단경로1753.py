import heapq
import sys
infinite = float("inf")
V, E = map(int,sys.stdin.readline().split())
K = int(input())
graph = [[] for _ in range(V+1)]
arr = [infinite]*(V+1)
for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))

def dijkstra(start):
    arr[start] = 0
    heap = []
    heapq.heappush(heap,(0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if arr[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < arr[i[0]]:
                arr[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

dijkstra(K)
for i in range(1,V+1,1):
    if arr[i] != infinite:
        print(arr[i])
    else:
        print("INF")