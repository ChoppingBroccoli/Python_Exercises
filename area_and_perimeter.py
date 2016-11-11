"""
This program asks the user for the radius of their circle then displays the
area and perimater of said circle.
"""


#Ask user for the radius of their circle and convert it to a float data type
radius=float(input("What is the radius of your circle, good Sir? "))

#Calculate the area
area=(radius*radius) * 3.14

#Calculate the perimeter
perimeter=(radius*2) * 3.14

#This was my original code before I discovered you can convert the input from the user to a float
"""
area=(float(radius)*float(radius)) * 3.14
perimeter=(float(radius)*2) * 3.14
"""

#Print the area
print("The area of your circle is",area)

#Print the perimeter
print("The perimeter of your circle is",perimeter)
