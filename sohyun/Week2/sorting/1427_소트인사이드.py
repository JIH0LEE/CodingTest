n = input()
n = [int(i)  for i in n]

s = sorted(n, reverse=True)

for i in s:
    print(i, end="")