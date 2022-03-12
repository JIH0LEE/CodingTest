import sys
infinite = float("inf")

def bellmanFord(start):
    global N,M
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != infinite and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False

N,M = map(int,sys.stdin.readline().split())
edges = []
distance = [infinite]*(N+1)
for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append((a,b,c))

circular = bellmanFord(1)

if circular:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i] == infinite:
            print(-1)
        else:
            print(distance[i])
