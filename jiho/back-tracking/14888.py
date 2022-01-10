# 연산자 끼워넣기
import sys
input = sys.stdin.readline
n = int(input())
inputs = list(map(int, input().split()))
op_inputs = list(map(int, input().split()))
operators = []

max = -1000000000
min = 1000000000
visited = [False]*(n-1)
result = []
for i in range(4):
    for j in range(op_inputs[i]):
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        else:
            operators.append('/')


def calculate():
    rt = inputs[0]
    for idx, elem in enumerate(result):
        if elem == '+':
            rt = rt+inputs[idx+1]
        elif elem == '-':
            rt = rt-inputs[idx+1]
        elif elem == '*':
            rt = rt*inputs[idx+1]
        else:
            if rt < 0:
                rt = -(abs(rt)//inputs[idx+1])
            else:
                rt = rt//inputs[idx+1]

    return rt


def solve(cnt):
    global max
    global min
    if cnt == n-1:
        val = calculate()
        if val > max:
            max = val
        if val < min:
            min = val
        return
    for i in range(n-1):
        if not visited[i]:
            result.append(operators[i])
            visited[i] = True
            solve(cnt+1)
            result.pop()
            visited[i] = False


solve(0)
print(max)
print(min)
