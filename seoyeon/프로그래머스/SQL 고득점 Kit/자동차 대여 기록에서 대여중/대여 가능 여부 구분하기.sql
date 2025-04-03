--순서: from -> group by-> select -> order by
-- group by로 car_id가 하나의 그룹으로 묶임 -> select max()에서 각 그룹 내의 최댓값 구함
-- select max() 내에서 조건을 만족하면 1을 반환하여 대여중 출력 

select car_id,
    max(case when "2022-10-16" between start_date and end_date 
       then "대여중"
       else "대여 가능" end)
    as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc