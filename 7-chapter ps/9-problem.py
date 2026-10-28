word = "pomogranate"

d = {}
for i in word:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
