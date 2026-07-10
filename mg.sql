use uzair;

insert into stk(id,name,qty,rte) values ();
insert into cus(name,cre,deb,phno) values ('Uzair',45,56,123456);
insert into bro(id,name,cre,deb,phno) values (3,'uzair',0,1400,15623344);
insert into newuser(name,pass,mail,phno) values ('Uzair Ahmd',1420,'uzr@gmail.com',123456);
insert into stkhis (id,name,qty,rate,chngs) values (1,'Tshirt',500,100,'Added Stock');
insert into bchis (id,name,cre,deb,phno,chngs) values (1,'Syed Shahul',5000,2000,'Customer Created');

create table stk(id int not null primary key , name varchar(30), qty int , rte int);
create table cus(id int not null primary key auto_increment , name varchar(30), cre int , deb int , phno int);
create table bro(id int not null primary key auto_increment , name varchar(30), cre int , deb int , phno int);
create table newuser(name varchar(30) primary key,pass int(15),mail varchar(50),phno int(12));
create table stkhis (id int,name varchar(30),qty int,rate int,chngs varchar(200));
create table bchis (id int,name varchar(30),cre int,deb int,phno int,chngs varchar(200));
create table bill(id int not null primary key , name varchar(30), qty int , rte int , amt int);

drop table cus;

select * from stk;
select * from cus;
select * from bro;
select * from newuser;
select * from stkhis;
select * from bchis; 
truncate bill;
select * from bill;

select name from cus;

truncate table bill;

drop table bill;

select amt from bill;

select id from cus where name='Srinivas';
