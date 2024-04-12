create table car_brands (
		id int unsigned,
        title varchar(255)
    );

create table car_models (
	id int unsigned,
    car_brand_id int unsigned,
    title varchar(255)
    );
    
create table users (
	id int unsigned,
    firstName varchar(255),
    lastName varchar(255),
    email varchar(255),
    password varchar(255)
);

create table cars (
	id int unsigned,
    userId int unsigned,
    carBrandId int unsigned,
    carModelId int unsigned,
    mileage float,
    initialMileage float
);

    
	