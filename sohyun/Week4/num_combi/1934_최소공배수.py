n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    x , y = a, b

    while a % b != 0:
        a, b = b, a % b
    print(x * y // b)