# n과 m (2)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

visit = []


for i in range(n):
    visit.append(False)

result = []


def solve(cnt, idx):

    global n
    global m

    if cnt == m:
        for ele in result:
            print(ele, end=" ")
        print()
        return

    for i in range(idx, n):
        if visit[i]:
            continue
        visit[i] = True
        result.append(i+1)
        solve(cnt+1, i+1)
        visit[i] = False ""
        result.pop()


solve(0, 0)
