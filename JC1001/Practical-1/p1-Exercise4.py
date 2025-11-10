#4) Write a program that asks the user to enter first their height in feet, followed by the
#number of inches e.g. first the user may enter 5, followed by 8, meaning that their height
#is 5 feet, 8 inches. Your program should then return the user’s height in centimetres.
feet = int(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))
height_cm = (feet * 30.48) + (inches * 2.54)
print("Your height in centimetres is "+ str(height_cm) +" cm.")