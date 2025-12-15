#6)  Running on a treadmill at a constant speed burns 9.7 calories per minute. Write a 
#program that uses an iterative statement to display the number of calories burned 
#after 10, 15, 20, 25 and 30 minutes.
calories=0.0
for minute in range(1,31):
    calories+=9.7
    if minute in {10,15,20,25,30}:
        print("The calories burned after %d minutes is %.2f" % (minute, calories))
#p4-Exercise-6.py
