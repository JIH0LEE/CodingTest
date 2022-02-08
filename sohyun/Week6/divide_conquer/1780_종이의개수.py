n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

neg_ones = 0
zeros = 0
ones = 0

def check(x, y, n):
    global neg_ones, zeros, ones
    number = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if number != paper[i][j]:
                for k in range(3):
                    for p in range(3):
                        check(x + k * n // 3, y + p * n // 3, n // 3)
                return
    if number == -1:
        neg_ones += 1
        return
    elif number == 0:
        zeros += 1
        return
    else:
        ones += 1
        return

check(0, 0, n)
print(neg_ones)
print(zeros)
print(ones)