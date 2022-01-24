n = int(input())

def fact(n):
    if n>=2:
        return n*fact(n-1)
    else:
        return 1

for _ in range(n):
    n, m = list(map(int, input().split()))
    print(fact(m) // (fact(n) * fact(m-n)))