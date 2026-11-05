#reverse a string using recursion


# def rev(n):
#     if len(n) == 1:
#         return n
#     return n[-1] + rev(n[:-1])
# r = rev("hello")
# print(r)

# def rev(n):
#     if len(n) == 1:
#         return n
#     ans = rev(n[1:])+n[0]
#     return ans
# print(rev("Hello"))


# def fun(n):
#     if n == 0:
#         return

#     fun(n-1)
#     print(n)
#     fun(n-1)

# fun(3)

#print 1 to n recursively going way down
# def rec(n,i):
    
#     if n == 0:
#         return 
#     print(i)
#     i = i+1
#     rec(n-1,i)

# rec(3,1)

# def rec(n):
#     if n == 0:
#         return
#     rec(n-1)
#     print(n) #going way up

# rec(5) 

#sum of first n natural numbers recursively

# def add(n):
#     if n == 1:
#         return 1
#     return n + add(n-1)
# print(add(5))


# def num(n):
#     if n < 0:
#         return 
#     num(n-1)
#     print(n)

# num(5)