# 종이의 개수
import sys
input = sys.stdin.readline

n = int(input())
plus = 0
minus = 0
zero = 0
paper = [None for i in range(n)]
for i in range(n):
    paper[i] = list(map(int, input().split()))


def solve(arr):
    global plus
    global zero
    global minus
    try:
        size = len(arr)
    except:
        print(arr)
    target = arr[0][0]
    if size == 1:
        if target == 1:
            plus += 1
        elif target == -1:
            minus += 1
        else:
            zero += 1
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
            plus += 1
        elif target == -1:
            minus += 1
        else:
            zero += 1
        return
    else:
        solve([row[0:size//3] for row in arr[0:size//3]])
        solve([row[0:size//3] for row in arr[size//3:size*2//3]])
        solve([row[0:size//3] for row in arr[size*2//3:size]])
        solve([row[size//3:size*2//3] for row in arr[0:size//3]])
        solve([row[size//3:size*2//3] for row in arr[size//3:size*2//3]])
        solve([row[size//3:size*2//3] for row in arr[size*2//3:size]])
        solve([row[size*2//3:size] for row in arr[0:size//3]])
        solve([row[size*2//3:size] for row in arr[size//3:size*2//3]])
        solve([row[size*2//3:size] for row in arr[size*2//3:size]])


solve(paper)
print(minus)
print(zero)
print(plus)
