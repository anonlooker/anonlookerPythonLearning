# Program to compare lengths of two strings
a=input("Enter a string: ")
b=input("Enter the other string: ")
if len(a)>len(b):
    print("The first string is longer")
elif len(a)<len(b):
    print("The second string is longer")
else:
    print("Both strings are of equal length")
print("Length of first string:",len(a))
print("Length of second string:",len(b))
#strlen.py