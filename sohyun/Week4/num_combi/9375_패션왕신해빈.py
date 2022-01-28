n = int(input())

for i in range(n):
    num = int(input())
    dictionary = dict()
    res = 1
    for j in range(num):
        wear = input().split()
        if wear[1] in dictionary:
            dictionary[wear[1]] += 1
        else:
            dictionary[wear[1]] = 1
    for k in dictionary.values():
        res *= (k+1)
    res -= 1

    print(res)