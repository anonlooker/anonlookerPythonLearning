#5)  Write  a  function  that  receives  a list  of  integers  and  returns a  new  list  using  list 
#comprehension  to  calculate  the  square  of  each  element  if  the  square  of  each 
#element is > 50.
def squareGreaterThan50(int_list):
    squared_list = [n**2 for n in int_list if n**2 > 50]
    return squared_list
#p5-Exercise-5.py