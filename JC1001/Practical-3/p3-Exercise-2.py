#2)  Write a program that reads a letter from the English alphabet from the user. If the 
#letter is a vowel (a,e,i,o,u) then it should inform the user that it is a vowel. If the 
#user enters a (y), then the user should be informed that a y can sometimes be a 
#vowel and sometimes is not. For all other input letters, the program should inform 
#the user that it is a consonant.
letter = input("Enter a letter from the English alphabet: ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The letter '%s' is a vowel." % letter)
elif letter == 'y':
    print("The letter 'y' can sometimes be a vowel and sometimes is not.")
else:
    print("The letter '%s' is a consonant." % letter)
#p3-Exercise-2.py