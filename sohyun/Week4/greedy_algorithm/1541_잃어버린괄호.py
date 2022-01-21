s = input().split('-')
sum = 0

plus1 = s[0].split('+')
for i in range(len(plus1)):
    sum += int(plus1[i])

for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)