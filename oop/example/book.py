# base class

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def getDetails(self):
        print(f"Book {self.title} is written by {self.author}")

# child class EBook is inheriting from Book class
class EBook(Book):
    def __init__(self,title,author,type):
        super().__init__(title,author)
        self.type=type

    def getDetails(self):   # Method overriding
        print(f"Book {self.title}.{self.type} is written by {self.author}")

class AudioBook(Book):
    def __init__(self,title,author,narrator):
        super().__init__(title,author)
        self.narrator = narrator

    def getDetails(self):   # Method overriding
        print(f"Book {self.title}, written by {self.author} is narrated by {self.narrator}")



# polymorphism: same function that works differently for different books
 
def showBook(book):
    book.getDetails()


book1=Book("Sample","Abhi")
ebook1=EBook("Marvel","Stan Lee","pdf")
audiobook1=AudioBook("Harry Potter","J K Rowling","Rowl")

showBook(book1)
showBook(ebook1)
showBook(audiobook1)