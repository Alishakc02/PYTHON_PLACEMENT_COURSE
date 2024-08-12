#A python program to find the Gcd of two numbers
'''
GCD or HCF is the highest common 
factor that divides both the numbers

for eg:
HCF of 5 and 25 is 5

'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if num1<num2:
    min =num1
else:
    min=num2
    
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i
        
print(f"The HCF/GCD of the two numbers is {hcf}")