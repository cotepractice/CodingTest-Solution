-- 코드를 입력하세요
SELECT h.flavor
FROM FIRST_HALF h
INNER JOIN JULY j ON h.flavor = j.flavor
GROUP BY flavor
ORDER BY SUM(j.total_order)+SUM(h.total_order) DESC LIMIT 3