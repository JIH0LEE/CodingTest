# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
visited = [False for i in range(100001)]
visited[n] = True
count = 0
queue = deque([[n, count]])


def find_next(x):
    rt = []
    temp = [x-1, x+1, x*2]
    for elem in temp:
        if 0 <= elem <= 100000:
            rt.append(elem)
    return rt


while queue:
    x, cnt = queue.popleft()
    if x == k:
        print(cnt)
        break
    next = find_next(x)
    for elem in next:
        if not visited[elem]:
            queue.append([elem, cnt+1])
            visited[elem] = True
