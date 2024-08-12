#A program to check whether the given 
# string is palindrome or not
String1 = input('Enter the String :')

String2 = String1[::-1]

if String1 == String2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')