def fact(n):
    if n>=2:
        return n*fact(n-1)
    else:
        return 1

n = int(input())
print(fact(n))