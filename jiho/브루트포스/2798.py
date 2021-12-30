# 블랙잭

n, m = map(int, input().split())
inputs = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = inputs[i]+inputs[j]+inputs[k]

            if temp > result and temp <= m:
                result = temp
print(result)
