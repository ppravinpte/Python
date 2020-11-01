'''Provides error handling with customer errors '''
class ToomanyPagesReadError(ValueError): # Inherit from built-in exception error
     pass                                # these has methods to raise it as error.
#this is copy of ValueError with different name as 'ToomanyPagesReadError'.                              
class Book:
    def __init__(self, name: str, page_count: int): # name in str, page in int format.
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of total {self.page_count}>"
        )
    
    def read(self, pages: int): #pages in int format
        if self.pages_read + pages > self.page_count:
            raise ToomanyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages > total pages {self.page_count}"
            )

        self.pages_read += pages
        print(f"You have read {self.pages_read} out of {self.page_count} pages.")

"""
python101 = Book("Python 101", 50)
python101.read(35)
python101.read(50)

o/p:
You have read 35 out of 50 pages.
Traceback (most recent call last):
  File "custom_errhandling.py", line 26, in <module>
    python101.read(50)
  File "custom_errhandling.py", line 17, in read
    raise ToomanyPagesReadError(
__main__.ToomanyPagesReadError: You tried to read 85 pages > total pages 50 """

# Used try , except to throw user friendly error message.
python101 = Book("Python 101", 50)
try: 
    python101.read(35)
    python101.read(50)
except ToomanyPagesReadError as e:
    print(e)
#o/p:
#You have read 35 out of 50 pages.
#You tried to read 85 pages > total pages 50
