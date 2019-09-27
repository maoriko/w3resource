# 1. Write a Python program to print the following string in a specific format.
# Sample String:
# "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
print("Twinkle, twinkle, little star, \n    How I wonder what you are! \n       Up above the world so high,\n       Like a diamond in the sky.\nTwinkle, twinkle, little star,\n       How I wonder what you are")

# 2. Write a Python program to get the Python version you are using
import sys
print(f'Sample Output :\n{sys.version}')

# 3. 
import datetime
today  = datetime.date.today()
print(f'Current Date and time :\n{today}')

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

