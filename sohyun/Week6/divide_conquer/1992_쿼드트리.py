n = int(input())
paper = [list(map(int, input())) for _ in range(n)]

def check(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                print('(', end='')
                check(x, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if color == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return

check(0, 0, n)