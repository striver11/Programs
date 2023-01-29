l=[[1,2,3],[4,5,6],[7,8,9]]
# l=[[1,2],[4,5],[7,8]] this only have two diagonal elements[1,5] l
k=[]
'''
for i in l:
    for j in i:
        if i==j:
            k.append(i)
print(k)
'''

'''
for i in range(len(l)):
    for j in range(len(l[i])):
        if i==j:
            print(i,j)
            k.append(l[i][j])
print(k)
'''

for i in range(len(l)):
    k.append(l[i][i])
print(k)
