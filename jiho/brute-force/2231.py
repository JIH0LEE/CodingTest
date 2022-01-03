# 분해합

# 1부터 N부터 확인해보자

n = int(input())
result = 0
for i in range(1, n):
    sum = i
    k = i
    while True:

        sum += k % 10
        k = k//10
        if k == 0:
            break
    if sum == n:
        result = i
        break
print(result)
