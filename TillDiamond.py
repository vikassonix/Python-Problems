num=3
till=4
for i in range(num,num+till):
    for j in range(num,i+1):
        print(i,end="")
    print("")
for i in range(num+till-2,num-1,-1):
    for j in range(num,i+1):
        print(i,end="")
    print("")