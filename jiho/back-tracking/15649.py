# n과 m (1)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

visit = []


for i in range(n):
    visit.append(False)

result = []


def solve(cnt):

    global n
    global m

    if cnt == m:
        for ele in result:
            print(ele, end=" ")
        print()
        return

    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        result.append(i+1)
        solve(cnt+1)
        visit[i] = False
        result.pop()


solve(0)
