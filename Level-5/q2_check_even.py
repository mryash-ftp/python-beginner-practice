with open("data.txt","r") as f:
    for i in f:
        if int(i)%2==0:
            a=int(i)/2
            print(int(a))
