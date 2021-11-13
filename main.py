from decorators.Entity import Entity
from datetime import date

@Entity("authors")
class Author():
    def __init__(self, name: str, birth_date: date, death_date: date=None):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date

    def __str__(self):
        return f"{self.name} ({self.birth_date.year}-{self.death_date.year if self.death_date != None else 'Alive'})"





@Entity("books")
class Books():

    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


def main():
    author = Author("J.K. Rowling", date(1965, 7, 31))
    book = Books("Python", author)
    print(book)

if __name__ == '__main__':
    print("calling main")
    main()