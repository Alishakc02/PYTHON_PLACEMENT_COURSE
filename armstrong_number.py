#Program to check whether the 
# given number is armstrong or not
num = input("Enter a number: ")
x = len(num)
sum = 0
for i in range(x):
    y =int(num[i])**x
    sum += y
if sum == int(num):
    print(f'{num} is an Armstrong number')
else:
    print(f'{num}is not an Armstrong number')