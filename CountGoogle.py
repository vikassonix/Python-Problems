s="google"
print("Program to count letters GOOGLE")
a=list(s)
b=set(a)
c=list(b)
c.sort()
for i in range(0,len(c)):
    print(c[i],s.count(c[i]))
