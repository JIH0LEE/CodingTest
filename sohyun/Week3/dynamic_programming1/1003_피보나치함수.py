n = int(input())

for i in range(n):
    s = int(input())
    zero = 1
    one = 0
    new_one = 0
    for _ in range(s):
        new_one = one + zero
        zero = one
        one = new_one
    print(zero, new_one)