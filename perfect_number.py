# WAP IN PYTHON TO CHECK WHETHER THE 
# GIVEN NUMBER IS PERFECT NUMBER OR NOT

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))


def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))

gcdFunction(num1, num2)