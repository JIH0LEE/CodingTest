# 운동
import sys
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())
graph = [[INF  for i in range(v+1)] for j in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, v+1):
    # i를 거쳐가는 것을 탐색
    for j in range(1, v+1):
        # j에서 시작
        for k in range(1, v+1):
            # k는 도착지
            # j->i->k
            if graph[j][k] > graph[j][i]+graph[i][k]:
                graph[j][k] = graph[j][i]+graph[i][k]
rt=INF
for i in range(1,v+1):
    rt = min(rt, graph[i][i])
if rt==INF:
    print(-1)
else:
    print(rt)
            