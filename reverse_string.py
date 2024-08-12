#A python program to reverse a string

def reverse_string(str):  
# Declaring empty string to store the reversed string  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
# It will return the reverse string to the caller function  
    return str1  
# Given String     
str = "Pycoding"         
print("The original string is: ",str)  
# Function call  
print("The reverse string is",reverse_string(str)) 
