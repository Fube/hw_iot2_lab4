from decorators.Entity import Entity
from datetime import date

@Entity("authors")
class Author():
    name: str
    birth_date: date
    death_date: date


@Entity("books")
class Books():
    title: str
    author: Author


def main():
    author = Author()
    author.name = "John Doe"
    author.birth_date = date(1955, 1, 1)
    author.death_date = date(2000, 1, 1)

    book = Books()
    book.title = "The Lord of the Rings"
    book.author = author

    print(book.save())
    print(book.get_all())

if __name__ == '__main__':
    print("calling main")
    main()