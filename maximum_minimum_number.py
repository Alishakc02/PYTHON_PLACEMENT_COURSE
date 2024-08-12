#Program to find the maximum and minimum 
# element from the arrray of elemnts

#Maximum Element
arr=[12,3,4,67,90,54]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)

#Minimum Element
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
        
print(min)
