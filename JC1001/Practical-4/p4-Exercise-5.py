#5)  A  weather  station  records  the  average  temperature  every  day  for  7  days.  Write  a 
#program  that  allows  the  user  to input the  temperature  each  day for  7  days  and  then 
#displays the average temperature for that week. 
sumTemp=0
for i in range(7):
    tempToday=float(input(f"Temperature on day {i+1}: "))
    sumTemp+=tempToday
avgTemp=sumTemp/7
print(avgTemp)
#p4-Exercise-5.py