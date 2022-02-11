# 선택정렬
n = int(input())
s = []

for i in range(n):
    s.append(int(input()))

for i in range(len(s) - 1):
    tmp = i
    for j in range(i + 1, len(s)):
        if(s[tmp] >= s[j]):
            tmp = j
    s[i], s[tmp] = s[tmp], s[i]

for i in range(n):
    print(s[i])