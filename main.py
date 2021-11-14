from db.relationships import OneToMany
from decorators.Entity import Entity
from datetime import date

@Entity("authors")
class Author():
    name: str
    birth_date: date
    death_date: date
    books: OneToMany("books", "author_id", "id")


@Entity("books")
class Book():
    title: str
    author_id: int


def main():
    author = Author()
    author.name = "John Doe"
    author.birth_date = date(1955, 1, 1)
    author.death_date = date(2000, 1, 1)

    book = Book()
    book.title = "The Lord of the Rings"

    author.books.add(book)

    book = Book()
    book.title = "The Hobbit"

    author.books.add(book)

    author.save()

if __name__ == '__main__':
    main()