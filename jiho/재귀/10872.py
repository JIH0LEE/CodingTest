# 팩토리얼

def solve(n):
    if n == 1 or n == 0:
        return 1

    return n*solve(n-1)


n = int(input())
print(solve(n))
