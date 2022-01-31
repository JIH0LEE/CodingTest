# 오큰수
n = int(input())
inputs = list(map(int, input().split()))
stack = [0]
result = [-1 for i in range(n)]
for i in range(1, n):

    elem = inputs[i]
    while True:
        if not stack:
            stack.append(i)
            break
        else:
            if elem > inputs[stack[-1]]:
                result[stack.pop()] = elem
                continue
            else:
                stack.append(i)
                break


for elem in result:
    print(elem,end=" ")
