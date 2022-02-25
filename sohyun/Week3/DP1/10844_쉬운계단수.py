n = int(input()) # n : 자릿수

s = [[0]*10 for _ in range(n+1)]
# 1자리 수
for i in range(1, 10):
    s[1][i] = 1

# 2자리수 이상
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            s[i][0] = s[i-1][j+1]
        elif j == 9:
            s[i][9] = s[i-1][j-1]
        else:
            s[i][j] = s[i-1][j-1] + s[i-1][j+1]

print(sum(s[n]) % 1000000000)
