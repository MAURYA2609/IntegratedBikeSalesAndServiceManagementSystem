create database ibssms;

use ibssms;

drop table if exists users;

create table users(
	id integer primary key auto_increment,
    username varchar(255) not null,
    password varchar(255) not null,
    user_type varchar(255) default "customer"
);

select * from users;