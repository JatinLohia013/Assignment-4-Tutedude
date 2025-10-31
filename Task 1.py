try:
    with open("Sample.txt","r") as fin:
        data=fin.readlines()
        for i in range(len(data)):
            print(f"Line {i}: ",data[i].strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not Found")
except:
    print("Any other Error")