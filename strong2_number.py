num=int(input("Enter a number:"))
sum=0

temp = num
while (num>0):
    digit = num%10
    fact = 1
    for i in range (1, digit+1):
        fact = fact*i
    sum = sum+fact
    num = num//10
if (sum==temp):
     
    print( 'Strong Number')
else:

    print ('Not a Strong Number')