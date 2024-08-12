#A python program to print the alphabetical pyramid
'''
A
B B
C C C
D D D D
E E E E E
F F F F F F
'''

rows=int(input("Enter the number of rows:"))
ascii_value=65 #(A=65)
#outer loop for rows
for i in range(rows):
#inner loop for column
    for j in range(i+1):
#gives corresponding alphabet to the given ascii value
        alphabet=chr(ascii_value)
#prints the given alphabet
        print(alphabet,end=" ")
#ascii value is increased by 1
    ascii_value+=1
    print()