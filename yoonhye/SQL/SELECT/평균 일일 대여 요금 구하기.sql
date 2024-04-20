-- ROUND(num, i) => i가 양수인 경우, 소수점 i번째 자리까지 유지하고 그 뒤의 숫자를 반올림.
-- ROUND(num, 1)이면 소수 첫 번째 자리에서 반올림한다는 의미
SELECT ROUND(avg(DAILY_FEE), 1) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = "SUV";