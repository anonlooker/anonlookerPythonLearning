class Book:
    isbn=int()
    def printIsbn(self):
        print(self.isbn)

whyNationlsFails=Book()
whyNationlsFails.isbn=1234567890
whyNationlsFails.printIsbn()