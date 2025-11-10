#3) Write a program which converts temperature in degrees Fahrenheit to degrees
#Celsius. Your program should include in the output, the original value in
#Fahrenheit that has been converted into degrees Celsius. (a simple way to
#perform this calculation is to deduct 32 from the Fahrenheit temperature, multiply
#by 5 and then divide by 9).
fahrenheitTemp = float(input("Enter temperature in degrees Fahrenheit: " ))
celsiusTemp = (fahrenheitTemp - 32) * 5 / 9
print("%f degrees Fahrenheit is equal to %f degrees Celsius." % (fahrenheitTemp, celsiusTemp))
#p2-Exercise-3.py