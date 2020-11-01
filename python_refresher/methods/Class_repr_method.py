''' Class method:'''
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

#book = Book("Harry Potter", "hardcover", 5)
#print(book)       # o/p: <__main__.Book object at 0x0070E808> 
                   # ned to use str, repr method to display content'
#print(book.name)  # o/p: Harry Potter

    def __repr__(self): # this method recreate a book object
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}gm>"
        
#book = Book("Harry Potter", "hardcover", 5)
#print(book)       #o/p: #o/p: <Book Harry Potter, hardcover, weighing 5gm>

    @classmethod   # class method using paper-type from variable. Not passed via parameter.
    def hardcover(cls, name, paper_weight):
        return Book(name, Book.TYPES[0], paper_weight+100)
 
    @classmethod
    def paperback(cls, name, paper_weight):
        return Book(name, Book.TYPES[1], paper_weight)


book = Book.hardcover("Harry Potter", 5)
light = Book.paperback("paper book", 2)
print(book)  # o/p: <Book Harry Potter, hardcover, weighing 105gm>
print(light) # o/p: <Book paper book, paperback, weighing 2gm>
'''
