import random

def listpro():

    my_list=[]

    for i in range(1,8):

        num=random.randint(1,30)

        my_list.append(num)

    a=sorted(set(my_list))

    print(a)


    print("Largest:",max(a))

    print("Min:",min(a)) 

    a.remove(max(a))

    print("2 Largest :",max(a))
    
    s_list=[]

    for i in my_list:

        if i%2==0:

            s_list.append(i)
        
    print(s_list)

    b=my_list

    for j in b:

        a=j

        temp=0

        for i in str(a):

            temp+=int(i)**3

        if a==temp:

            print("Its Armstrong",a)

        else:

            print("Not Armstrong",a)

    for j in b:

        a=j

        temp=0

        for i in range(1,int(a/2)+1):

            if a%i==0:

                temp=temp+i

        if j==temp:        

            print("Perfect Number",j)

        else:

            print("Not a Perfect Number",j)
listpro()
