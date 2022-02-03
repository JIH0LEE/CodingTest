# 쿼드 트리
import sys
input = sys.stdin.readline

n = int(input())

paper = [None for i in range(n)]


def solve(arr):

    size = len(arr)

    target = arr[0][0]

    if size == 1:
        if target == '1':
            return '1'
        else:
            return '0'

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
        if target == '1':
            return '1'
        else:
            return '0'

    else:
        return '(' + solve([row[0:size//2] for row in arr[0:size//2]])+solve([row[size//2:size] for row in arr[0:size//2]])+solve([row[0:size//2] for row in arr[size//2:size]])+solve([row[size//2:size] for row in arr[size//2:size]])+')'


for i in range(n):
    paper[i] = input().rstrip()
print(solve(paper))
