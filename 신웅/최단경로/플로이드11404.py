import sys
infinite = float("inf")

n = int(input())
m = int(input())
graph = [[infinite]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c 

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd()
for i in range(n):
    for j in range(n):
        if graph[i][j] == infinite:
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()