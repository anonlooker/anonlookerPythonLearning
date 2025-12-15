#2)  Write a function that receives a list of integers and returns a list that only contains 
#odd numbers from the original list. 
def filterOddNumbers(intList):
    oddList = []
    for n in intList:
        if n%2:
            oddList.append(n)
    return oddList

#p5-Exercise-2.py