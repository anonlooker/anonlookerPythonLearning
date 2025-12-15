#6)  Write  a  function  that  receives  a  list  of  strings  containing  duplicate  values  and 
#returns a new list with all duplicates removed.
def removeDuplicates(stringList):
    noDuplicatesList = []
    for s in stringList:
        if s not in noDuplicatesList:
            noDuplicatesList.append(s)
    return noDuplicatesList
#p5-Exercise-6.py