from collections import deque
import sys

def bfs(x,y):
    

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))
