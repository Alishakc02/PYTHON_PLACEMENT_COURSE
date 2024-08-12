# A python program to print the simple alphabetical pyramid
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''

rows=int(input("Enter the number of rows:"))
for num in range(rows+1):
    for i in range(num):
        print(num,end=" ")
    print()