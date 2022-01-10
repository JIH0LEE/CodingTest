# 스타트와 링크
import sys
input = sys.stdin.readline
n = int(input())
status_table = []
for i in range(n):
    status_table.append(list(map(int, input().split())))
all = [i for i in range(n)]
visited = [False for i in range(n)]
start = []
min = 1000000000


def calculate():
    link = list(set(all)-set(start))
    sum1 = cal(start)
    sum2 = cal(link)

    return abs(sum1-sum2)


def cal(arr):
    rt = 0
    for i in range(len(arr)):
        elem1 = arr[i]
        for j in range(i+1, len(arr)):

            elem2 = arr[j]
            rt = rt+status_table[elem1][elem2]+status_table[elem2][elem1]
    return rt


def solve(cnt, idx):
    global min
    if cnt == n//2:
        temp = calculate()
        if temp < min:
            min = temp

    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                start.append(i)
                solve(cnt+1, i+1)
                start.pop()
                visited[i] = False


solve(0, 0)
print(min)
