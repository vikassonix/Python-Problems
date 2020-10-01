s1="abcd"
s2="bcad"
a1=list(s1)
a2=list(s2)
a1.sort()
a2.sort()
print(a1,a2)
flag=0
for i in range(0,len(a1)):
    if(a1[i]==a2[i]):
        flag=0
    else:
        flag=1
        break

if(flag):
    print("Not anagram")
else:
    print("Anagram")