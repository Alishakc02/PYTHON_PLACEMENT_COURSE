#Python program for insertion sort
#Note the indentation

def insertionSort(array):
    
    for i in range(1,len(array)) :
        key=array[i]
        j=i-1
#Arranging the elemnts in increasing order
        while j>=0 and key<array[j]:
          array[j+1]=array[j]
          j=j-1
# Place key at after the element just smaller than it.
        array[j + 1] = key

data=[2,6,9,1,3,8,5,8]
#Calling function
insertionSort(data)
print("The sorted array is:")
#Output
print(data)


