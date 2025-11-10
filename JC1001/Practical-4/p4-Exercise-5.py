sumTemp=0
for i in range(7):
    tempToday=float(input(f"Temperature on day {i+1}: "))
    sumTemp+=tempToday
avgTemp=sumTemp/7
print(avgTemp)
#p4-Exercise-5.py