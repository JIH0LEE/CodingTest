# 신나는 함수 실행
import sys
input = sys.stdin.readline

dp = dict()
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            dp[(i, j, k)] = None
inputs = []
while True:
    temp = tuple(map(int, input().split()))
    if temp == (-1, -1, -1):
        break

    inputs.append(temp)


def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return solve(20, 20, 20)

    else:

        if dp[(a, b, c)]:
            return dp[(a, b, c)]
        else:
            if a < b and b < c:
                dp[(a, b, c)] = solve(a, b, c-1) + \
                    solve(a, b-1, c-1)-solve(a, b-1, c)
            else:
                dp[(a, b, c)] = solve(a-1, b, c)+solve(a-1, b-1, c) + \
                    solve(a-1, b, c-1)-solve(a-1, b-1, c-1)

            return dp[(a, b, c)]


for elem in inputs:
    a, b, c = elem
    print("w({}, {}, {}) = {}".format(a, b, c, solve(a, b, c)))
