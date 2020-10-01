n = 5
a = 1
for i in range(1, n+1):
    for j in range(1,i):
        print(f"{a} * ",end="")
        a+=1
    print(a)
    a=a+1
        
a-=1
for i in range(n,0,-1):
    x = ""
    for j in range(1,i):
        if (j==1):
            x = f"{a} " + x
        else:
            x = f"{a} * " + x
        a-=1
    if(a==1):
        print(a)
    else:
        print(a,"*",x)
    a=a-1

