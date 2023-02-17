select * from dojos;
select * from ninjas;
-- insert  dojo name
insert into dojos (name)
values ('miami-dojo'),
	   ('chicago-dojo'),
       ('michigan_dojo');
       
insert into ninjas (first_name, last_name, age, dojo_id)
values 
('miguel','garcia',18,1),
('john','perez',21,1),
('kayla','fernandez',28,1),
('juan','lopez',34,2),
('dylan','sanchez',42,2),
('rafael','sanchez',23,2),
('randy','orta',23,3),
('dercik','romero',25,3),
('chris','busta',25,3);
-- join
select * from ninjas
join dojos
on ninjas.dojo_id = dojos.id
where dojo_id = 1;
-- last dojo
select * from ninjas
join dojos
on ninjas.dojo_id = dojos.id
where dojo_id = 3;
select * from ninjas
join dojos
on ninjas.dojo_id = dojos.id
where ninjas.id = 10;