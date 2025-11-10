#5)  Write a program that determines the name of a shape from its number of sides. 
#Read the number of sides from the user and then report the appropriate name as 
#part of a meaningful message. Your program should support shapes with 
#anywhere from 3 up to (and including) 10 sides. If the number of sides outside of 
#this range is entered, then your program should display an appropriate error 
#message.
sides = int(input("Enter the number of sides of the shape (3-10): "))
if sides == 3:
    shape_name = "Triangle"
elif sides == 4:
    shape_name = "Quadrilateral"
elif sides == 5:
    shape_name = "Pentagon"
elif sides == 6:
    shape_name = "Hexagon"
elif sides == 7:
    shape_name = "Heptagon"
elif sides == 8:
    shape_name = "Octagon"
elif sides == 9:
    shape_name = "Nonagon"  
elif sides == 10:
    shape_name = "Decagon"
else:   
    shape_name = None
if shape_name:
    print(f"A shape with {sides} sides is called a {shape_name}.")
else:
    print("Error: The number of sides must be between 3 and 10.")
#p3-Exercise-5.py