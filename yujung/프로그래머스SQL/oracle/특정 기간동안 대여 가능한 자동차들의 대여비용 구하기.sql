select c.car_id, c.car_type, floor((c.daily_fee*((100-d.DISCOUNT_RATE)/100))*30) as fee
from (
    SELECT a.car_id, a.car_type, a.daily_fee
    from CAR_RENTAL_COMPANY_CAR a
    where a.car_id not in (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where to_char(START_DATE, 'YYYYMM') = '202211' or to_char(END_DATE, 'YYYYMM') = '202211'
    )
    and a.CAR_TYPE in ('세단','SUV') 
) c
,CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
where c.CAR_TYPE = d.CAR_TYPE
and d.DURATION_TYPE LIKE '30%'
and floor((c.daily_fee*((100-d.DISCOUNT_RATE)/100))*30) BETWEEN 500000 and 2000000
order by 3 desc, 2, 1 desc