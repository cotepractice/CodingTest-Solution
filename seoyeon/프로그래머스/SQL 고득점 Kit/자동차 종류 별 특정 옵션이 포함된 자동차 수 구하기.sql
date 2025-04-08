select c.CAR_TYPE, count(car_type) as CARS
from car_rental_company_car c
where c.options like "%통풍시트%" or c.options like "%열선시트%" or c.options like "%가죽시트%"
group by c.car_type
order by c.car_type