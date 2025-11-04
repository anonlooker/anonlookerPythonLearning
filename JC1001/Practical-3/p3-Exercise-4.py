#4)  In the Gregorian calendar, the length of a month varies from 28 to 31 days. Write 
#a program that reads the name of a month from the user as a string. Then 
#displays the number of days in that month.  
# 
#Hint: If the month is Feb, then it should display “28 or 29 days” to take leap years 
#into account.
month = input("Enter the name of a month: ").strip().lower()
if month in ['january', 'jan', 'march', 'mar', 'may', 'jul', 'july', 'aug', 'august', 'oct', 'october', 'dec', 'december']:
    print(f"{month.capitalize()} has 31 days.")
elif month in ['april', 'apr', 'june', 'jun', 'september', 'sep', 'november', 'nov']:
    print(f"{month.capitalize()} has 30 days.")
elif month in ['february', 'feb']:
    print("February has 28 or 29 days.")
else:
    print("Invalid month name entered.")
#p3-Exercise-4.py