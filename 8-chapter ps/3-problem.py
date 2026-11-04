#recursion reverse string
# s = "hello"
# g = ""
# for i in range(len(s)-1, -1, -1):
#     g += s[i]
# print(g)

# for i in s:
#     g = i+g
# print(g)
print(rev("hello"))
def rev(n):
    g = ""
    l = len(n)
    if n == -1:
        return ""
    return 