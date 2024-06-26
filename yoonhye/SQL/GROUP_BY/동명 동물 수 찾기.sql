-- SQL에서 NULL은 '값이 없음'을 의미하며, IS NULL이나 IS NOT NULL을 통해서만 올바르게 검사할 수 있다.
SELECT NAME, count(*) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING count(*) >= 2
ORDER BY NAME