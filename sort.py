sort=[1,6,0,1,1,9,7,0]
for i in range(len(sort)):
    for j in range(i+1,len(sort)):
        if sort[i]>sort[j]:
            sort[i],sort[j]=sort[j],sort[i]
print(sort)