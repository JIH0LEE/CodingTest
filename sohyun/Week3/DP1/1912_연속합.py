n = int(input())
s = list(map(int, input().split()))

new_s = [0] * n
new_s[0] = s[0]

for i in range(1, len(s)):
    new_s[i] = max(s[i], new_s[i-1] + s[i])

print(max(new_s))