#2)  The 1p Saving Challenge is a year-long challenge you can start on the 1st of 
#January 2022. It involves saving a little money every day, starting with 1p. The 
#next day you save 2p, the day after 3p. Write a program that tells the user how 
#much money they end up with at the end of the year.
moneyNow=0
for moneyToday in range(1, 366):
    moneyNow+=moneyToday
print(f"You have {moneyNow}p money at the end of the year.")
#p4-Exercise-2.py