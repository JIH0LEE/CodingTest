# 미확인 도착지
import sys
from heapq import heappop,heappush
input=sys.stdin.readline
INF = 100000000

T=int(input())

def dijktra(start, end):
    
    global n
    costs = [INF for _ in range(n+1)]
    costs[start] = 0
    priority_queue = []
    heappush(priority_queue, (0, start))
    while priority_queue:
        w, e = heappop(priority_queue)
        for adj, weight in graph[e]:
            new_weight = w+weight
            if new_weight < costs[adj]:
                costs[adj] = new_weight
                heappush(priority_queue, (new_weight, adj))
    return costs[end]

for _ in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    goal=[]
    result=[]
    for i in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    for i in range(t):
        goal.append(int(input()))
    
    for end in goal:
        first=dijktra(s,g)+dijktra(g,h)+dijktra(h,end)
        second=dijktra(s,h)+dijktra(h,g)+dijktra(g,end)
        min_length=dijktra(s,end)
        rt=min(first,second)

        if rt==min_length:
            result.append(end)
    result.sort()

    for elem in result:
        print(elem,end=" ")
    print()
    


    

