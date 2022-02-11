def decompose(n):
    for i in range(1, n + 1):
        temp = sum(map(int, str(i)))
        res = i + temp

        if res == n:
            return i
        if i == n:
            return 0


n = int(input())
print(decompose(n))