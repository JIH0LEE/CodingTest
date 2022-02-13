n = int(input())
li = list(map(int, input().split()))
stack = [0]
res = [-1 for _ in range(n)]

for i in range(1, n):
    x = li[i]
    while True:
        if not stack:
            stack.append(i)
            break
        else:
            if x > li[stack[-1]]:
                res[stack.pop()] = x
                continue
            else:
                stack.append(i)
                break


for i in res:
    print(i, end=' ')