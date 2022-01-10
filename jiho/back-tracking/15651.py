# n과 m (3)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


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

        result.append(i+1)
        solve(cnt+1)
        result.pop()


solve(0)
