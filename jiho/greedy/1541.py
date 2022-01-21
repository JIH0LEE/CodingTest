# 잃어버린 괄호
import sys
from collections import deque
input = sys.stdin.readline
line = input().strip()
op = deque()
tmp = ""
for c in line:
    if c == '+' or c == '-':
        op.append(tmp)
        op.append(c)
        tmp = ""
    else:
        tmp += c
op.append(tmp)
result = 0
while op:
    elem = op.popleft()
    if not elem:
        break
    if elem == '-':
        tmp_result = 0
        while op:

            elem1 = op.popleft()

            if elem1 == '-':
                op.appendleft(elem1)
                break
            else:

                if elem1 != '+':
                    tmp_result += int(elem1)

        result -= tmp_result

    else:
        if elem != '+':
            result += int(elem)

print(result)
