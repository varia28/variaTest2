alter table car_brands
	modify id int primary key auto_increment;

alter table car_models
	modify id int primary key auto_increment,
    modify car_brand_id int not null,
    add foreign key (car_brand_id) references car_brands(id); 
    
alter table users
	modify id int primary key auto_increment;
    
alter table cars
	modify id int primary key auto_increment,
    modify userId int not null,
    modify carBrandId int not null,
    modify carModelId int not null,
    add foreign key (userId) references users(id),
    add foreign key (carBrandId) references car_brands(id),
    add foreign key (carModelId) references car_models(id);
    
    insert into users(firstName,lastName,email,password) values ('john','smith', 'john@gg.ccc','2111');
    insert into users(firstName,lastName,email,password) values ('Rahul','Kumar', 'Rahul@gg.ccc','1112');
    insert into users(firstName,lastName,email,password) values ('Aakash','Roy', 'Aakash@gg.ccc','1121');
    insert into users(firstName,lastName,email,password) values ('Nick','Chorba', 'Aakash@gg.ccc','1211');
    
    insert into car_brands(title) values ('Maruti Suzuki');
    insert into car_brands(title) values ('Mahindra & Mahindra');
    insert into car_brands(title) values ('Tata Motors');
    
    insert into car_models(car_brand_id,title) values (2, 'Thar');
    insert into car_models(car_brand_id,title) values (2, 'Bolero');
    insert into car_models(car_brand_id,title) values (1, 'Jimny');
    insert into car_models(car_brand_id,title) values (1, 'Wagon R');
    insert into car_models(car_brand_id,title) values (1, 'Dzire');
    insert into car_models(car_brand_id,title) values (3, 'Curvv');
    
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (1,1,5,1000, 0);
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (2,2,1,1000, 0);
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (2,2,2,1000, 0);
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (3,3,6,1000, 0);
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (4,1,3,1000, 0);
    insert into cars(userId,CarBrandId,carModelId,mileage,initialMileage) values (4,1,5,1000, 0);

    