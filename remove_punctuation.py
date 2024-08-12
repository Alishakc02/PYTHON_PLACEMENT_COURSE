#A python program to remove punctuation from the
#given string
punc='''!()-[]{};:'"\,<>./?@#$%^&*~`'''
string = input("Enter anything here: ")

empty_str = ""


for i in string:
    if i not in punc:
      empty_str = empty_str + i
      
print(empty_str)