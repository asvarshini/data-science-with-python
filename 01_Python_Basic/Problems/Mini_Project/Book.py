class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def display(self):
        print(f"{self.title}: {self.pages}")


class LibraryManager:
    def __init__(self):
        self.lis = []

    def add(self, title, pages):
        book = Book(title, pages)
        self.lis.append(book)
        print(f"Added {title} with pages {pages}")

    def disall(self):
        print("\n--- Book List ---")
        for book in self.lis:
            book.display()

    def hig(self):
        if not self.lis:
            print("No books available")
            return
        max_book = max(self.lis, key=lambda book: book.pages)
        print(f"\nBook with highest pages: {max_book.title} ({max_book.pages})")


# Main
v = LibraryManager()
v.add("Alexa", 202)
v.add("Gram Bell", 404)
v.add("Hemisphere", 100)

v.disall()
v.hig()