#read&write
with open("4-problem.txt", "r+") as f:
    # content = f.read()
    # print(content)
    f.seek(0,2)
    f.write("\nGoing Merry is the 1st ship of the straw hats.")
    f.seek(0)
    print(f.read())
    