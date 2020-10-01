from math import sqrt 
x = 20
sq = [i*i for i in range(1,x+1)]
final = []
for i in sq:
    for j in sq:
        if (i+j) in sq:
            a = int(sqrt(i))
            b = int(sqrt(j))
            c = int(sqrt(i+j))
            s = set((a,b,c))
            if s not in final:
                final.append(s)
print(final)