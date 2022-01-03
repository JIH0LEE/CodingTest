# 덩치
n = int(input())
inputs = []
result = []
for i in range(n):
    inputs.append(list(map(int, input().split())))


for i in range(n):
    w, h = inputs[i]
    rank = 1
    for j in range(n):
        w1, h1 = inputs[j]
        if w < w1 and h < h1:
            rank += 1
    result.append(rank)

for elem in result:
    print(elem, end=" ")
