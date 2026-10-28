# word = "pomogranate"

# d = {}
# for i in word:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

"""
* * * 
*   *   for n = 3 
* * *  
"""
#pattern problem

# n = 3
# for i in range(1, n+1):
#     if (i == 1 or i ==n):
#         print("*" * n)
#     else:
#         print("*", end = "")
#         print(" "*(n-2), end = "")
#         print("*")

st = "lorry"
s = ""
# for i in range(len(st)-1, -1, -1):
#     s += st[i]
# s = st[::-1]

for i in st:
    s = i+s

print(s)
    

