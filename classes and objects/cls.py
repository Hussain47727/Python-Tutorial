class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", "Yes" if self.available else "No")

    def borrow(self):
        if self.available:
            print("You have borrowed the book.")
            self.available = False
        else:
            print("Sorry, the book is already borrowed.")


# ==== Using the class ====

# Create a book object
book1 = Book("The Alchemist", "Paulo Coelho", True)

# Show book info
book1.display_info()
print()

# Try to borrow the book
book1.borrow()

# Try to borrow again
book1.borrow()
print()

# Show updated book info
book1.display_info()
