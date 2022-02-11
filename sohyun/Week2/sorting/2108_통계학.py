from collections import Counter

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

# 산술평균
print(round(sum(s)/n))

# 중앙값
s.sort()
print(s[n//2])

# 최빈값
chk = Counter(s).most_common()
if len(chk)>1 and chk[0][1]==chk[1][1]:
    print(chk[1][0])
else:
    print(chk[0][0])

# 범위
print(max(s)-min(s))