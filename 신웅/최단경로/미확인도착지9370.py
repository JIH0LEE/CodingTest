import sys
import heapq
infinite = 100000000

def dijkstra(start, end):
    heap = []
    global node
    distance = [infinite]*(node+1)
    distance[start] = 0
    heapq.heappush(heap,(0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))
    return distance[end]
    
T = int(sys.stdin.readline())
for _ in range(T):
    node, road, targetNum = map(int,sys.stdin.readline().split())
    start, g, h = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(node+1)]
    for _ in range(road):
        a, b, c = map(int,sys.stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    target = []
    result = []
    for _ in range(targetNum):
        target.append(int(sys.stdin.readline()))
    endH = dijkstra(start,g) + dijkstra(g,h)
    endG = dijkstra(start,h) + dijkstra(h,g)
    for i in target:
        temp = dijkstra(start,i)
        path1 = endH + dijkstra(h,i)
        path2 = endG + dijkstra(g,i)
        shortest = min(path1,path2)
        if shortest == temp:
            result.append(i)
    result.sort()
    for elem in result:
        print(elem,end=" ")
    print()
    
    