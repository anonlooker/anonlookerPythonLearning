#8)  Write a program that reverses the calculation performed in exercise 7, where the 
#user enters a duration in seconds and the duration is returned to the user in days, 
#hours, minutes, and seconds, with each unit of time printed on a separate line.
totalSeconds = int(input("Enter duration in seconds: "))
days = totalSeconds // 86400
totalSeconds %= 86400
hours = totalSeconds // 3600
totalSeconds %= 3600
minutes = totalSeconds // 60
seconds = totalSeconds % 60
print("Duration:")
print("%d days" % days)
print("%d hours" % hours)
print("%d minutes" % minutes)
print("%d seconds" % seconds)
#p2-Exercise-8.py