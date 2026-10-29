#star pattern
# """
#   * 
#  *** 
# *****
# """
# n = 3
# for i in range (1, n+1):
#     print(" " * (n-i) + "*" * (i*2-1))

"""
*****
 ***
  *
"""

# n = 3
# for i in range (n,0,-1):
#     print(" " * (n-i) + "*" * (i*2-1))

"""
   *
  **
****
  **
   * 
"""

n = 7

# # Top half
# for i in range(1, n):
#     print(" " * (n - i) + "*" * i)

# # Middle row
# print("*" * n)

# # Bottom half
# for i in range(n-1, 0,  -1):
#     print(" " * (n - i) + "*" * i)

'''
*
**
***
****
*****
******
*******
******
*****
****
***
**
*
'''

# Top half
for i in range(1, n):
    print("*" * i)

# Middle row
print("*" * n)

# Bottom half
for i in range(n-1, 0,  -1):
    print("*" * i)