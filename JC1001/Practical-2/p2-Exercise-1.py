#1) Write a program which asks the user for their name and age and then calculates
#the year of their birth and returns this information to the user.
import datetime
name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello %s. Your birth year is %d." % (name,datetime.datetime.now().year - age))
#p2-Exercise-1.py