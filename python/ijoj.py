sample=[1,2,3,4,5,10,11,33,1,2,5,7,9,9]
print("the given list:",sample)
count_dict=dict()
for i in sample:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1
print(count_dict)
