#링
import sys
from math import gcd
input=sys.stdin.readline
n=int(input())
inputs=list(map(int,input().split()))
a=inputs[0]
for i in range(1,n):
    b=inputs[i]
    gcd_value=gcd(a,b)
    print(str(a//gcd_value)+'/'+str(b//gcd_value))

