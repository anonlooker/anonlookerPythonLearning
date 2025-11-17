#4)  Write  a  function  that  receives  a  list  of  integers  and  returns  a  new  list  using  list 
#comprehension which contains each item from the original list, multiplied by 10.
def multiplyByTen(intList):
    multiplyedList = []
    for n in intList:
        multiplyedList.append(n * 10)
    return multiplyedList
#p5-Exercise-4.py