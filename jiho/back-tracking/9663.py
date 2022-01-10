# N-Queen
# 실패... 시간초과 왜?


import sys
input = sys.stdin.readline
n = int(input())
result = []

ans = 0


def check(n):

    length = len(result)
    for i in range(length):
        pos = length-i
        if (n == result[i]) or (abs(n - result[i]) == pos):
            return False
    return True


def solve(cnt):

    global ans
    if cnt == n:
        ans += 1

        return

    for i in range(0, n):
        is_valid = check(i)
        if is_valid:
            result.append(i)
            solve(cnt+1)
            result.pop()
        else:
            continue


solve(0)
print(ans)
