d = {}

for i in range (1,5):
    name = input("Enter your name: ")
    lan = input("Enter your fav language: ")
    d.update({f"{name}":f"{lan}"})
print(d.items())

'''
taking friends name and fav language as user input
'''