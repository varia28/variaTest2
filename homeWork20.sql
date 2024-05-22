alter table car_brands
	modify id int primary key auto_increment;

alter table car_models
	modify id int unsigned primary key auto_increment,
    modify car_brand_id int not null,
    add foreign key (car_brand_id) references car_brands(id); 
    
alter table users
	modify id int primary key auto_increment;
    
alter table cars
	modify id int unsigned primary key auto_increment,
    modify userId int not null,
    modify carBrandId int not null,
    modify carModelId int unsigned not null,
    add foreign key (userId) references users(id),
    add foreign key (carBrandId) references car_brands(id),
    add foreign key (carModelId) references car_models(id);
    
create table expenses (
    id int unsigned primary key auto_increment,
    model_id int unsigned not null,
    car_id int unsigned not null,
    date date not null,
    liters_used float,
    total_cost decimal(10,2),
    foreign key (model_id) references car_models(id),
    foreign key (car_id) references cars(id)
);

    
insert into users(firstName,lastName,email,password) values ('john','smith', 'john@gg.ccc','2111');
insert into users(firstName,lastName,email,password) values ('Rahul','Kumar', 'Rahul@gg.ccc','1112');
insert into users(firstName,lastName,email,password) values ('Aakash','Roy', 'Aakash@gg.ccc','1121');
insert into users(firstName,lastName,email,password) values ('Nick','Chorba', 'Aakash@gg.ccc','1211');
insert into users(firstName,lastName,email,password) values ('Mahat','Gayview', 'GayviewMahat@gg.ccc','1213');
insert into users(firstName,lastName,email,password) values ('poor','gav', 'GayviewMahat@gg.ccc','1213');


insert into car_brands(title) values ('Maruti Suzuki');
insert into car_brands(title) values ('Mahindra & Mahindra');
insert into car_brands(title) values ('Tata Motors');
insert into car_brands(title) values ('Audi');
insert into car_brands(title) values ('BMW');

insert into car_models(car_brand_id,title) values (2, 'Thar');
insert into car_models(car_brand_id,title) values (2, 'Bolero');
insert into car_models(car_brand_id,title) values (1, 'Jimny');
insert into car_models(car_brand_id,title) values (1, 'Wagon R');
insert into car_models(car_brand_id,title) values (1, 'Dzire');
insert into car_models(car_brand_id,title) values (3, 'Curvv');
insert into car_models(car_brand_id,title) values (4, 'R8');
insert into car_models(car_brand_id,title) values (4, 'TT');
insert into car_models(car_brand_id,title) values (5, '3');
insert into car_models(car_brand_id,title) values (5, '5');
    
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (1,1,5,123, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (2,2,1,444, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (2,2,2,4564, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (3,3,6,23423, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (4,1,3,233, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (4,1,5,100, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (5,4,7 ,44, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (5,4,8 ,67, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (1,5,9 ,27, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (1,5,10,47, 0);
insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (1,5,9 ,16, 0);

insert into expenses(model_id, car_id, date, liters_used, total_cost) values (5,1,'2024-05-03', 3, 3.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (1,2,"2024-05-03", 3.5, 3.50);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (2,3,"2024-05-03", 10, 10.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (6,4,"2024-05-03", 1, 1.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (3,5,"2024-05-03", 2.55, 2.55);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (5,6,"2024-05-03", 5, 5.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (7 ,7,"2024-05-03", 1, 1.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (8 ,8,"2024-05-03", 4, 4.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (9 ,9,"2024-05-03", 4, 4.00);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (10,10,"2024-05-03", 3.1, 3.10);
insert into expenses(model_id, car_id, date, liters_used, total_cost) values (9 ,11,"2024-05-03", 3.5, 3.50);

    