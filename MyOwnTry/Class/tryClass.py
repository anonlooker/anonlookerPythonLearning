class object:
    """
    Base class for all classes
    """
    name=str()
    def printName(self):
        print(self.name)
class Book(object):
    isbn=int()
    def printIsbn(self):
        print("ISBN of \""+ self.name + "\" is " + str(self.isbn))
whyNationlsFail=Book()
whyNationlsFail.name="Why Nations Fail"
whyNationlsFail.isbn=1234567890
whyNationlsFail.printIsbn()