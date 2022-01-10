# 스도쿠
# python3 시간초과 pypy3 통과

import sys
input = sys.stdin.readline

sdk = []
zeros = []

for i in range(9):
    sdk.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            zeros.append((i, j))


def solve(cnt):

    if cnt == len(zeros):

        for line in sdk:
            for elem in line:
                print(elem, end=" ")
            print()
        sys.exit(0)

    x = zeros[cnt][0]
    y = zeros[cnt][1]

    x1 = (x//3)*3
    y1 = (y//3)*3

    is_valid_num = [False] + [True for i in range(9)]

    # 가로 세로 검사
    for i in range(9):
        if sdk[x][i]:
            is_valid_num[sdk[x][i]] = False
        if sdk[i][y]:
            is_valid_num[sdk[i][y]] = False

    # 3x3검사
    for i in range(x1, x1+3):
        for j in range(y1, y1+3):
            if(sdk[i][j]):
                is_valid_num[sdk[i][j]] = False

    valid_nums = [i for i, k in enumerate(is_valid_num) if k == True]

    for num in valid_nums:
        sdk[x][y] = num
        solve(cnt+1)
        sdk[x][y] = 0


solve(0)
