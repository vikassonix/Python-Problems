s="abcde5fghijklmn51opqrstuwxyvz1"
l=list(s)
x=len(l)
for i in s:
    if(i.isdigit()):
        l.remove(i)  

a=set(l)
if(len(a)==26):
    print("Panagram")
else:
    print("Not Panagram")