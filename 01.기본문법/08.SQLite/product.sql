-- SQLite
select * from juso;

create table product(
    code integer primary key AUTOINCREMENT,
    name char(100),
    price integer DEFAULT 0
);

select * from product;

insert into product(name, price)
values('LG 세탁기', 2500000);
insert into product(name, price)
values('LG 냉장고', 3500000);