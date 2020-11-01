# In below inheritance example, there is nothing used in Book class
# that's inherited from BookShelf. So there is no use of defining.

# Inheritance Example here.
'''
class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __str__(self):
        return f"Bookshelf with {self.quantity} books."
        # Bookshelf with 300 books.
    
shelf = BookShelf(300)
print(shelf)
# o/p: Bookshelf with 300 books.

class Book(BookShelf): # quantity not used still need to mentioned.
    def __init__(self, name, quantity):  
        super().__init__(quantity)
        self.name = name

    def __str__(self):  # not used str of bookshelf.
        return f"Book {self.name}"

book = Book("Harry Potter", 120)
print(book)
'''
#################
## Composition used below##
class BookShelf:
    def __init__(self, *books): # number of inputs.
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
        # Bookshelf with 300 books.
    
#shelf = BookShelf('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A14')
#print(shelf)
# o/p: Bookshelf with 13 books.

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python")
book3 = Book("Panda")
book4 = Book("Numpy")

shelf = BookShelf(book, book2, book3, book4)
print(shelf)
# o/p: Bookshelf with 4 books.
print(shelf.books)
# o/p: Gives output (<__main__.Book object at 0x0047E820>, 
#<__main__.Book object at 0x00514DA8>, <__main__.Book object at 0x00514D90>, 
#<__main__.Book object at 0x00506880>)
