#reverse a string using recursion


# def rev(n):
#     if len(n) == 1:
#         return n
#     return n[-1] + rev(n[:-1])
# r = rev("hello")
# print(r)

def rev(n):
    if len(n) == 1:
        return n
    ans = rev(n[1:])+n[0]
    return ans
print(rev("Hello"))