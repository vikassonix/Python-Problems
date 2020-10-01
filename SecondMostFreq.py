arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3]
s = set(arr)
sl = list(s)
sl.sort()
k = []
v = []
for i in range(0, len(sl)):
    t = int(arr.count(sl[i]))
    k.append(sl[i])
    v.append(t)

m1 = max(v)
for i in range(len(v)-1, -1, -1):
    if(v[i] == m1):
        v[i] = 0
        break

m2 = max(v)
loc = 0
for i in range(0, len(v)):
    if(v[i] == m2):
        loc = k[i]
        break

print(loc)
