'''PYTHON MINI PROJECT - TO CHECK IF A RANDOM NUMBER GENERATED WITHIN A GIVEN RANGE IS A PRIME/COMPOSITE,
 ODD/EVEN AND POSITIVE/NEGETIVE.'''


import random
n=int(input("Enter no of times you want to take the range: "))
for i in range(0,n):
    a=int(input("Enter range a(starting range):"))
    b=int(input("Enter range b(ending range):"))
    y=random.randrange(a,b)
    print("The random number between range",a,"and",b,"is",y)
    if y>0:
        print(y,"is a positive number")
        if y%2==0:
            print(y,"is an even number")
        else:
            print(y,"is an odd number")
    elif y==0:
        print(y,"is neither positive nor negetive")
        print(y,"is neither odd nor even")
    else:
        print(y,"is a negetive number")
        print(y,"is neither odd nor even")
    if y>1:
        for i in range(2,int(y/2)+1):
            if (y % i) ==0:
                print(y,"is a composite number")
                break
        else:
            print(y,"is a prime number")
    elif(y==0 or y==1):
        print(y,"is neither prime nor composite")
    else:
        print(y,"is neither prime nor composite")
