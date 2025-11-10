#4)  Below you have the algorithm of a program that asks the user for a set of positive 
#numbers and identifies the highest among them. The user enters the number 0 to 
#finish the sequence. Implement the algorithm below and test it. 
# 
#Set number with number entered by user  
# Set highest  with number 
#while number is not 0 
#if number is greater than highest  
#Set highest with number 
# 
#Set number with number entered by user  
#print highest
number = int(input("Enter a positive number (0 to finish): "))
highest = number
while number != 0:
    if number > highest:
        highest = number
    number = int(input("Enter a positive number (0 to finish): "))
print(highest)
#p4-Exercise-4.py