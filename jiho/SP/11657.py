# 타임머신
# 벨만-포드 알고리즘
import sys
input = sys.stdin.readline
INF = 1000000000
n, m = map(int, input().split())
edges = []
costs = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def belman_ford(start):
    global n, m
    costs[start] = 0
    for i in range(n):
        for elem in edges:
            a, b, c = elem
            if costs[a] != INF and costs[b] > costs[a]+c:
                costs[b] = costs[a]+c
                if i == n-1:
                    return False
    return True


if not belman_ford(1):
    print(-1)
else:
    for elem in costs[2:]:
        if elem == INF:
            print(-1)
        else:
            print(elem)
