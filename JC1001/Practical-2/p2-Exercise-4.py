#4) Write a program that reverses the calculation performed in exercise 4.
#That is, it should convert a temperature in degrees Celsius to degrees Fahrenheit.
#Include in the output, the original value in Celsius that has been converted into
#degrees Fahrenheit. (a simple way to perform this calculation is to multiply the
#Celsius temperature by 9, divide by 5 and then add 32).
celsiusTemp = float(input("Enter temperature in degrees Celsius: " ))
fahrenheitTemp = (celsiusTemp * 9 / 5) + 32
print("%f degrees Celsius is equal to %f degrees Fahrenheit." % (celsiusTemp, fahrenheitTemp))
#p2-Exercise-4.py