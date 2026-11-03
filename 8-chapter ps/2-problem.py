# def fact(n):
#     if n == 0:
#         return 1

#     ans = n * fact(n-1)
#     return ans

# fact(5)

# def count(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         return n - count(n-1)
        
# count(5)

#sum of n
def add(n):
    if n <=1 :
        return 1
    return n + add(n-1)
print(add(5))