#Python program to implement bubble sort

def bubbleSort (array):
    #loop to access each array element
    for i in range(len(array)):
    #loop to compare each array element
        for j in range(0,len(array)-i-1):
    #compare the each adjacent element
    # with each other
    
         if array[j]>array[j+1]:
             #swap the osition of the element if they
             #are not in intended order
             
           temp=array[j]
           array[j]=array[j+1]
           array[j+1]=temp

data=[2,7,3,9,14,10]
#calling the function 
bubbleSort(data)
print("The sorted array in ascending order is:")
#print the data
print(data)