'''
LCM is a non-zero number that is
least and multiple of both numbers

For eg:
The LCM of 4 and 6 is 12
'''
# defining a function to calculate LCM  
def calculate_lcm(num1, num2):  
    # selecting the greater number  
    if num1>num2:  
       max = num1  
    else:  
      max = num2
    while(True):  
        if((max % num1 == 0) and (max % num2 == 0)):  
            lcm = max  
            break  
        max += 1  
    return lcm    
  
# taking input  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the LCM 
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  
