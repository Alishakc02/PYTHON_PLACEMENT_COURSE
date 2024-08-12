#Python program to find the area and 
# circumfernce of the circle
from math import pi
radius=float(input('Enter the radius of circle'))
print(radius)
#calculating area and circumference of the circle
circumference=2*pi*radius
area=pi*radius**2
#printing the area and circumference of the circle
print("The area of the circle is:",area)
print("The cicumference of the circle is:",circumference)
