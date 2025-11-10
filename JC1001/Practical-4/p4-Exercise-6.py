calories=0.0
for minute in range(1,31):
    calories+=9.7
    if minute in {10,15,20,25,30}:
        print("The calories burned after {%d} minutes is {%.2f}",{minute,calories})
#p4-Exercise-6.py
