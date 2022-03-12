import sys
import heapq
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

infinite = float("inf")
def dijkstra(start, end):
    heap = []
    global N
    distance = [infinite]*(N+1)
    distance[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))
    return distance[end]

first, second = map(int, sys.stdin.readline().split())
path1 = dijkstra(1,first) + dijkstra(first,second) + dijkstra(second, N)
path2 = dijkstra(1,second) + dijkstra(second, first) + dijkstra(first, N)
if path1 != infinite or path2 != infinite:
    print(min(path1,path2))
else:
    print(-1)
