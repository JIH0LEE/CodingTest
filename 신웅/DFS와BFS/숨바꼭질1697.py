def operation(x, i):
    if i == 0:
        return x+1
    elif i == 1:
        return 2*x
    else :
        return x-1

def bfs():
    global N, K
    if N == K :
        print(0)
        return
    queue = deque()
    queue.append(N)
    while queue:
        temp = queue.popleft()
        for i in range(3):
            next = operation(temp,i)
            if next == K:
                print(graph[temp]+1)
                return
            if next < 0 or next > 100000:
                continue
            if graph[next] == 0:
                queue.append(next)
                graph[next] = graph[temp] + 1


import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())
graph = [0]*100001
bfs()