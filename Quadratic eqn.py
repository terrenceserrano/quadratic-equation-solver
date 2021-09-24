# create a program that will solve the quadratic eqn

from math import *

a = int(input("Enter coefficeint A: "))
b = int(input("Enter coefficient B: "))
c = int(input("Enter coefficient C: "))

d = int((b**2) - (4 * a * c)) #this is for the descriminant formula

if d > 0:
    root1 = int( (-b + (sqrt((b**2)- 4 * a * c)))/2 * a)
    root2 = int( (-b - (sqrt((b**2)- 4 * a * c)))/2 * a)
    print("Here is your roots 1 and 2: " + str(root1) + " and " + str(root2) + ", " + "the roots are distinct and real")
elif d == 0:
    root1 = root2 = int(-b/(2 * a))
    print("Here is your roots: " + str(root1) + "," + "the roots are equal and real")
else:
    root1 = int(-b / (2 * a))
    root2 = int(sqrt(-d / (2 * a)))
    print("Here is you roots 1 and 2: " + str(root1) + ", " + str(root2) + ", " + "the roots are imaginary")
