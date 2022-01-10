# n과 m (4)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


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
        result.append(i+1)
        solve(cnt+1, i)
        result.pop()


solve(0, 0)
