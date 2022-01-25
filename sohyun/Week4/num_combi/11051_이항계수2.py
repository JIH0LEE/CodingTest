n, k = map(int, input().split())

def fact(n):
    if n>=2:
        return n*fact(n-1)
    else:
        return 1

res = fact(n) // (fact(k)*fact(n-k))
print(res % 10007)