from datetime import date
from schemas.Author import Author
from schemas.Book import Book


def main():
    author = Author()
    author.name = "John Doe"
    author.birth_date = date(1955, 1, 1)
    author.death_date = date(2000, 1, 1)

    book = Book()
    book.title = "The Lord of the Rings"
    book.number_of_pages = 1234
    book.publication_date = date(1954, 1, 1)

    author.books.add(book)

    book = Book()
    book.title = "The Hobbit"
    book.number_of_pages = 5678
    book.publication_date = date(1937, 1, 1)

    author.books.add(book)
    
    author.save()

    # Update
    author.name = "Jane Doe"
    book.title = "The Hobbit 2"
    author.save()


    print([book.id for book in author.books.get()])

    #author.delete()

if __name__ == '__main__':
    main()