n = int(input())
word = []

for i in range(n):
    w = input()
    cnt = len(w)
    word.append((w, cnt))

word = list(set(word))
word.sort(key = lambda x: (x[1], x[0]))

for x in word:
    print(x[0])