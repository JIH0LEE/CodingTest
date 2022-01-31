# 스택 수열
import sys
input = sys.stdin.readline
n = int(input())
op = []
stack = []
count = 1
flag = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        flag = False
        break
if not flag:
    print('NO')
else:
    for elem in op:
        print(elem)
