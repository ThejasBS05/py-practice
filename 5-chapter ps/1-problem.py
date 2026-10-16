# d = {
#     "name" : "Thejas",
#     "age" : 23,
#     "company" : "Allegion India",
#     "language" : "Python"
# }

# # print(d.items())
# d.update({"name": "Darshan"})
# print(d.get("name"))
# print(d["name"])

# s = set()
# s.add("18")
# s.add(18)
# print(s)

# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?
# print(len(s))
# print(s)

a = {}
print("Enter 4 names and language\n")
name = input("Enter friend name:\n")
language = input("Enter fav language:\n")
a.update({name:language})
name = input("Enter friend name:\n")
language = input("Enter fav language:\n")
a.update({name:language})
name = input("Enter friend name:\n")
language = input("Enter fav language:\n")
a.update({name:language})
name = input("Enter friend name:\n")
language = input("Enter fav language:\n")
a.update({name:language})
print(a)