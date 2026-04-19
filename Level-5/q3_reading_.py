with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(f"Line found: {line.strip()}") 
