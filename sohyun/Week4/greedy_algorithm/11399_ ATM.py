n = int(input())
s = list(map(int, input().split()))
sum = 0
sorted_list = []

s.sort()
for i in range(n):
    for j in range(i + 1):
        sum += s[j]

print(sum)