#write and read

with open("5-problem.txt", "w+") as f:
    f.write("Ace is a brother for Luffy.")
    f.seek(0)
    content = f.read()
    print(content)
