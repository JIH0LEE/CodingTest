# 색종이 만들기
import sys
input = sys.stdin.readline

n = int(input())
blue = 0
white = 0
paper = [None for i in range(n)]


def solve(arr):
    global white
    global blue
    size = len(arr)
    target = arr[0][0]
    if size == 1:
        if target == 1:
            blue += 1
        else:
            white += 1
        return

    is_paper = True
    flag = False

    for elems in arr:
        for elem in elems:
            if target != elem:
                flag = True
                is_paper = False
                break
        if flag:
            break

    if is_paper:
        if target == 1:
            blue += 1
        else:
            white += 1
        return
    else:
        solve([row[0:size//2] for row in arr[0:size//2]])
        solve([row[0:size//2] for row in arr[size//2:size]])
        solve([row[size//2:size] for row in arr[0:size//2]])
        solve([row[size//2:size] for row in arr[size//2:size]])


for i in range(n):
    paper[i] = list(map(int, input().split()))

solve(paper)
print(white)
print(blue)
