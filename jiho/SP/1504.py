import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 100000000
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijktra(start, end, not_via=False):
    global N
    costs = [INF for _ in range(N+1)]
    costs[start] = 0
    priority_queue = []
    heappush(priority_queue, (0, start))
    while priority_queue:
        w, e = heappop(priority_queue)
        if not_via:
            if e == not_via:
                continue
        for adj, weight in graph[e]:
            new_weight = w+weight
            if new_weight < costs[adj]:
                costs[adj] = new_weight
                heappush(priority_queue, (new_weight, adj))
    return costs[end]


first = dijktra(1, v1)+dijktra(v1, v2)+dijktra(v2, N)
second = dijktra(1, v2)+dijktra(v2, v1)+dijktra(v1, N)
if first >= INF or second >= INF:
    print(-1)
else:
    print(min(first, second))
