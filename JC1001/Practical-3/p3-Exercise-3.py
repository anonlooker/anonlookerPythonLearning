#3)  Write a program that asks the user for the length and width of two rooms. It 
#should then inform the user whether the areas are the same, or if not, which room 
#is larger.
length1 = float(input("Enter the length of room 1: "))
width1 = float(input("Enter the width of room 1: "))
length2 = float(input("Enter the length of room 2: "))
width2 = float(input("Enter the width of room 2: "))
area1 = length1 * width1
area2 = length2 * width2
if area1 == area2:
    print("Both rooms have the same area: %f" % area1)
elif area1 > area2:
    print("Room 1 is larger with an area of: %f" % area1)
else:
    print("Room 2 is larger with an area of: %f" % area2)
#p3-Exercise-3.py