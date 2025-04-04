SELECT p.product_id, p.product_name,sum(o.amount)*p.price as total_sales
FROM food_product p
LEFT JOIN food_order o ON o.product_id = p.product_id
WHERE year(o.produce_date)="2022" and month(o.produce_date)="05"
GROUP BY o.product_id
ORDER BY total_sales DESC, p.product_id