n = int(input())
m = int(input())
graph = [[] * n for _ in range(n + 1)] # 경로저장

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0 # visit한 횟수 count
visited = [0] * (n + 1) # visit한 정점 확인


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i) # visit하지 않은 정점이면 재귀
            cnt += 1


dfs(1)
print(cnt)