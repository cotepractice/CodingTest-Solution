-- 내 코드: "특정 월의 총 대여 횟수가 0인 경우 제외" 조건 해결 못함
SELECT month(START_DATE), CAR_ID, COUNT(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE "2022-08" <= date_format(START_DATE,"%Y-%m") <= "2022-10"
GROUP BY month(START_DATE), CAR_ID
HAVING RECORDS>=5
ORDER BY month(START_DATE), CAR_ID DESC

-- 2 틀렸습니다
SELECT month(START_DATE), CAR_ID, COUNT(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE "2022-08" <= date_format(START_DATE,"%Y-%m") <= "2022-10"
    and CAR_ID in (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE "2022-08" <= date_format(START_DATE,"%Y-%m") <= "2022-10" GROUP BY CAR_ID HAVING COUNT(CAR_ID)>=5) 
GROUP BY month(START_DATE), CAR_ID
HAVING RECORDS>=1
ORDER BY month(START_DATE), CAR_ID DESC

--3 정답. date_format은 between을 사용해 해결
SELECT month(START_DATE), CAR_ID, COUNT(HISTORY_ID) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE date_format(START_DATE,"%Y-%m") BETWEEN "2022-08" and "2022-10"
    and CAR_ID in (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE date_format(START_DATE,"%Y-%m") BETWEEN "2022-08" and "2022-10" GROUP BY CAR_ID HAVING COUNT(CAR_ID)>=5) 
GROUP BY month(START_DATE), CAR_ID
HAVING RECORDS>=1
ORDER BY month(START_DATE), CAR_ID DESC

--4.의문. 왜 where에 date 관련 조건이 하나 더 있어야 하지?
select month(start_date), car_id, count(car_id) as records
from car_rental_company_rental_history

where car_id in (select car_id from car_rental_company_rental_history where date_format(start_date,"%Y-%m") between "2022-08" and "2022-10" group by car_id having count(car_id)>=5)

group by month(start_date), car_id
having records >= 1
order by month(start_date), car_id desc