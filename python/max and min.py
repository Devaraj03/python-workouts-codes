# ip:arr[]={10,20,4}
arr=[11,22,33,2,3,456,789]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print("the maximum number is:",max)
arr=[11,22,33,2,3,456,789]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print("the minimum num is ",min)
        
