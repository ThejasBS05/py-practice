#palindrome using recursion
# a=""
# def pal(n,a,i):
#     if i == len(n):
#         return ""
    
#     return pal(n,a,i+1) + n[i] 

# print(pal("thejas","",0))
# # if "mom" == b:
# #     print("palindrome")
# # else:
# #     print("not palindrome")

def rev(n):
    if len(n) == 1:
        return n
    return n[-1]+rev(n[:-1])

print(rev("Thejas"))