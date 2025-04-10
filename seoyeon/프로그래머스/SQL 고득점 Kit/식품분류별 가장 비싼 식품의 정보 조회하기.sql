select category, price as max_price, product_name
from food_product
where price in (select max(price) from food_product group by category)
    and (category="과자" or category="국" or category="김치" or category="식용유")
order by price desc