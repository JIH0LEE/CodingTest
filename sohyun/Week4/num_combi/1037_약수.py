n = int(input())
s = list(map(int, input().split()))

s.sort()
print(s[0] * s[n-1])