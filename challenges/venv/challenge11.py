class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def getDetails(self):
        return self.name + " by " + self.author

class ChildrensBook(Book):
    def __init__(self, name, author, age):
        Book.__init__(self,name, author)
        self.age = age

    def getDetails(self):
        return self.name + " by " + self.author + ". Suitable for children aged " + str(self.age)


book1 = Book("The hungry catterapillar", "Greg")
print(book1.getDetails())

book2 = ChildrensBook("The Gruffalo", "Julia Donaldson", 6)
print(book2.getDetails() )
