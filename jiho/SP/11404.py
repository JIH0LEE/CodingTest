# 플로이드
# 플로이드-와샬 알고리즘
import sys
input = sys.stdin.readline
INF = 1000000000
n = int(input())
m = int(input())

graph = [[0 if i == j else INF for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for i in range(1, n+1):
    # i를 거쳐가는 것을 탐색
    for j in range(1, n+1):
        # j에서 시작
        if i == j:
            continue
        for k in range(1, n+1):
            # k는 도착지
            if k == j or k == i:
                continue
            # j->i->k
            if graph[j][k] > graph[j][i]+graph[i][k]:
                graph[j][k] = graph[j][i]+graph[i][k]

for elem in graph[1:]:
    for a in elem[1:]:
        if a == INF:
            print(0, end=" ")
        else:
            print(a, end=" ")
    print()
