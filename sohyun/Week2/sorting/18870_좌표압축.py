n = int(input())
li = list(map(int, input().split()))
li2 = sorted(list(set(li)))

dic = {li2[i] : i for i in range(len(li2))}
for j in li:
    print(dic[j], end = ' ')