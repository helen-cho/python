/*테이블 생성*/
create table juso(
       seq int primary key autoincrement, 
       name char(20), 
       address char(200)
);

/*테이블 삭제*/
drop table juso;

/*데이터(행) 입력*/
insert into juso(name, address)values('홍길동', '인천서구 경서동');
insert into juso(name, address)values('심청이', '경기도 광명시');

/*데이터 확인*/
select * from juso;

/*데이터(행)삭제*/
delete from juso where seq=2;

/*데이터 수정*/
update juso set name='김길동', address='서울 강남구 압구정동' where seq=1;

select * from juso where name like '%동%' order by name desc;
select * from juso order by address desc;
 
create table product(
    code integer primary key AUTOINCREMENT,
    name char(100),
    price integer DEFAULT 0
);

select * from product;

insert into product(name, price)
values('LG 오브제 세탁기', 2500000);
insert into product(name, price)
values('LG 오브제 냉장고', 3500000);
 