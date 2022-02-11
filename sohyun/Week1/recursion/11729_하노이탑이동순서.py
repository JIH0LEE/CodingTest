def hanoi(n, bar1, bar3):
    if n == 1:
        print(bar1, bar3)
        return

    hanoi(n - 1, bar1, 6 - bar1 - bar3)
    print(bar1, bar3)
    hanoi(n - 1, 6 - bar1 - bar3, bar3)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)