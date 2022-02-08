n = int(input())
count = 0
stack = []
res = []
# impossible = True

for i in range(0, n):
    s = int(input())

    while count < s:
        count += 1
        stack.append(count)
        res.append("+")

    if s == stack[-1]:
        stack.pop()
        res.append("-")
    # else:
    #     impossible = False
    #     exit(0)

# if impossible == False:
#     print("NO")
# else:
print("\n".join(res))