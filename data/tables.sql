/*
    用户访问记录表
*/

drop table if exists visit_record;
create table visit_record(
    id int primary key auto_increment,
    appid int,
    user_name varchar(24),
    visit_time timestamp
)engine=innodb;

/*
    部门表，包含部门编号、部门名称
*/
drop table if exists dept;
create table dept(
    id int primary key auto_increment,
    dept_num int,
    dept_name varchar(64)
)engine=innodb;

/*
    员工表，包含员工姓名、入职时间、薪水、部门编号
*/

drop table if exists emp;
create table emp(
    id int primary key auto_increment,
    ename varchar(64),
    hiredate date,
    salary decimal(10, 2), 
    dept int(2)
)engine=innodb;


