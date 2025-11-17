#1)  Write a function that receives a string as a parameter and returns the text in the 
#string without vowels. 
# 
#e.g. print(withoutVowels(“No Vowels please”))  
#returns n  v w ls pl  s
def withoutVowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

#p5-Exercise-1.py