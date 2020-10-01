web = ['Bullet Bike Review',
       'Bike Review',
       'Review Bullet',
       'Review Bike',
       'Bullet Bike']
find = "bike"
find = find.lower()
k = [0]*len(web)
v = [-1]*len(web)
for i in range(0, len(web)):
    web[i] = web[i].lower()
    web[i] = web[i].split(" ")

for i in range(0, len(web)):
    for j in range(0, len(web[i])):
        if(web[i][j].startswith(find)):
            k[i] = i
            v[i] = j
            break
        else:
            k[i] = i
print(web)
print(k, v)
res = ''
for i in range(0, len(k)):
    for j in range(0, len(v)):
        if(i == v[j]):
            res += 'P'+str(j+1)+','
print(res[0:len(res)-1])
