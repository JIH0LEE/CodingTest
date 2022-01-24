#팩토리얼 0의 갯수
import sys
input=sys.stdin.readline

n=int(input())
def solve(n):
    count2=0
    count5=0
    for i in range(2,n+1):
        num2=i
        num5=i
        while True:
            if num2%2 !=0:
                break
            count2+=1
            num2=num2//2
        while True:
            if num5%5 !=0:
                break
            count5+=1
            num5=num5//5

    return min(count2,count5)
print(solve(n))