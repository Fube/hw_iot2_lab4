create table authors(
    id int not null auto_increment,
    name varchar(255) not null,
    birth_date date not null,
    death_date date default null,
    primary key(id)
);