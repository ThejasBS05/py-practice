#append and read

with open("6-problem.txt", "a+") as f:
    f.write("\nAce is a brother for Luffy.")
    f.seek(0)
    content = f.read()
    print(content)
