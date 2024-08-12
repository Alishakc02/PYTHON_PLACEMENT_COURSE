# Write a python program to get the execution time

import time  #Import time module
start = time.time() #record start time
a = 0  #sample code 
for i in range(1000):
	a += (i**100)
end = time.time() #record end time
#print the difference between start 
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms") #end time in milliseconds
