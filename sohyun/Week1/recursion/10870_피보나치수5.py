def fibo(n):
    if n>=2:
        return fibo(n-1)+fibo(n-2)
    else:
        return n

n = int(input())
print(fibo(n))