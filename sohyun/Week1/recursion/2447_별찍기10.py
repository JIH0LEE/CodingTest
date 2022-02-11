s = []


def star(i, j, n):
    if ((i // n) % 3 == 1 and (j // n) % 3 == 1):
        s.append(' ')
    else:
        if (n >= 3):
            star(i, j, n // 3)
        else:
            s.append('*')


n = int(input())

for i in range(n):
    for j in range(n):
        star(i, j, n)
    print(''.join(s), end="\n")
    s = []