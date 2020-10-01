till=3
for i in range(0,till):
    for j in range(1,i+2):
        if((j)!=i+1):
            print(i+1,"*",end="")
        else:
            print(i+1,end="")
    print("")

for i in range(till-1,-1,-1):
    for j in range(1,i+2):
        if((j)!=i+1):
            print(i+1,"*",end="")
        else:
            print(i+1,end="")
    print("")