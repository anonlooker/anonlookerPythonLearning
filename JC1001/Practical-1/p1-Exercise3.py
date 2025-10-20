#3) Write a program which asks the user to enter their name and age. The program should
#then output a message that returns this information and calculates the year the user will
#be 100 years old.
from datetime import datetime

now = datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = now.year + (100 - age)
print(str(name)+", you will be 100 years old in the year "+ str(year) + ".")