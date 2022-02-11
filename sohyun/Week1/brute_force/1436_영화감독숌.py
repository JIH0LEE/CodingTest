def director(n):
    tri_six = 666
    cnt = 0

    while True:
        if '666' in str(tri_six):
            cnt += 1
        if cnt == n:
            return tri_six
        tri_six += 1


n = int(input())
print(director(n))