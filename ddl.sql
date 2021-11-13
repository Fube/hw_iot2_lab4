create table authors(
    id int not null auto_increment,
    birth_date date not null,
    death_date date default null,
    primary key(id)
);