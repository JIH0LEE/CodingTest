#별찍기 -10

# 재귀로 출력하는 것이 아닌 list에 string 을 저장한다.

def solve(n):
    if n == 3:
        return ['***',
                '* *',
                '***']
    else:
        new = []
        arr = solve(n//3)
        for i in range(3):
            for j in range(n//3):
                if i == 0 or i == 2:
                    new.append(arr[j]+arr[j]+arr[j])
                else:
                    new.append(arr[j]+(' '*(n//3))+arr[j])
        return new


n = int(input())
rt = solve(n)

for elem in rt:
    print(elem)
