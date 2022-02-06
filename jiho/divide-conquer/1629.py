#곱셈
a,b,c=map(int,input().split())
def multi(a,b):
    global c
    return a*b%c

def solve(a,b):
    global c
    if b==1:
        return a%c
    elif b==2:
        return multi(a,a)
    else:
        temp=solve(a,b//2)
        if b%2==0:
            return multi(temp,temp)
        else:
            return multi(multi(temp,temp),a)

print(solve(a,b))