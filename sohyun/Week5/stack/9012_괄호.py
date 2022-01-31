n = int(input())

for i in range(n):
    b = input()
    stack = list(b)
    cnt = 0

    for i in stack:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break

    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')