create table authors(
    id int not null auto_increment,
    name varchar(255) not null,
    birth_date date not null,
    death_date date default null,
    primary key(id)
);

create table books(
    id int not null auto_increment,
    title varchar(255) not null,
    number_of_pages int not null,
    publication_date date not null,
    author_id int not null,
    primary key(id),
    foreign key(author_id)
        references authors(id)
        on delete cascade
);