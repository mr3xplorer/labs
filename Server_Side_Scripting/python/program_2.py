class Book:
    def __init__(self, id, author, price):
        self.id = id
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book({self.id}, {self.author}, {self.price})"

book1 = Book(1, "J.K. Rowling", 20)
book2 = Book(2, "Stephen King", 30)
book3 = Book(3, "Harper Lee", 40)
book4 = Book(4, "Ernest Hemingway", 50)

print(book1)
print(book2)
print(book3)
print(book4) 