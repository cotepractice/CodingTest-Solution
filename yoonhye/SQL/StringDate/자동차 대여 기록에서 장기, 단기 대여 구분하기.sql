-- IF(expression, value_if_true, value_if_false) : 조건을 만족하면 value_if_true, 만족하지 않으면 value_if_false 반환
-- DATEDIFF(date1, date2) : 두 날짜 간의 차이를 일 수로 반환
-- 이 문제에서 주의할 점은 실제 대여기간이 DATEDIFF(date1, date2) + 1이므로,
-- 대여기간이 30일 이상이라는 조건을 만족하려면 DATEDIFF(date1, date2)는 29보다 크거나 같아야 한다는 것이다.
SELECT HISTORY_ID,
       CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       IF(DATEDIFF(END_DATE,START_DATE)>=29, '장기 대여', '단기 대여') AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC