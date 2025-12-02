class object:
    """Base class for all objects"""
    name=str()
    def printName(self):
        print(self.name)
class Book(object):
    """Class representing a book"""
    isbn=int()
    def printIsbn(self):
        print("ISBN of \""+ self.name + "\" is " + str(self.isbn))
whyNationlsFail=Book()
whyNationlsFail.name="Why Nations Fail"
whyNationlsFail.isbn=1234567890
whyNationlsFail.printIsbn()