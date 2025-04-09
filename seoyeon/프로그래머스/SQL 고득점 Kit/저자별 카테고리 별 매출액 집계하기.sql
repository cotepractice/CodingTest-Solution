select b.author_id, a.author_name, b.category,sum(s.sales*b.price) as total_sales
from book_sales s
join book b on s.book_id = b.book_id
join author a on b.author_id = a.author_id 
where year(s.sales_date)=2022 and month(s.sales_date)=1
group by b.category, b.author_id
order by b.author_id, b.category desc