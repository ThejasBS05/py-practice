with open("story.txt", "r") as f:
    data = f.read()
    print(len(data)) #prints number of characters present
    words = data.split()
    print(len(words)) #prints the number of words present
    f.seek(0)
    line = f.readlines()
    print(len(line)) #prints the number of words present
    
