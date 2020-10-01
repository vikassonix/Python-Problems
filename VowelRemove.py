v="aeiouAEIOU"
s="ave"
for i in v:
    if(i in s):
        s=s.replace(i,"")
print(s)