select * from users where firstName like '%am%';

select max(liters_used) as "max litres audi" 
	from expenses join cars on car_id=cars.id join car_brands on cars.carBrandId=car_brands.id 
	where car_brands.title = "Audi" ;

select car_models.car_brand_id as "car_id", count(car_models.title) as "count_models"
	from car_brands join car_models on car_models.car_brand_id=car_brands.id 
    where car_brands.title="audi" or car_brands.title="BMW" 
    group by car_models.car_brand_id;
    
select car_models.title as "car_model", car_brands.title as "car_brand" , count(cars.userId) as "user_count" 
	from cars join car_models on carModelId=car_models.id join car_brands on carBrandId=car_brands.id 
    group by cars.carModelId, car_brands.title;
    
select firstName, lastName  from users left join cars on users.id=cars.userId group by users.firstName, users.lastName having count(cars.id) > 0;