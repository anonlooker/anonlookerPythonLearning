#2) Write a program which converts miles into kilometres. Your program should first
#ask the user to enter a distance in miles to be converted and you should then
#return the converted distance in kilometres. Include in the output, the original
#value in miles that has been converted into kilometres. (1 kilometre is
#approximately 0.6214 miles)
miles = float(input("Enter distance in miles: "))
kilometres = miles / 0.6214
print("%f miles is equal to %f kilometres." % (miles, kilometres))
#p2-Exercise-2.py