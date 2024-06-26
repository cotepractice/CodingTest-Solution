SELECT USER.USER_ID AS USER_ID, USER.NICKNAME AS NICKNAME, sum(BOARD.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS BOARD, USED_GOODS_USER AS USER
WHERE BOARD.STATUS = 'DONE' AND BOARD.WRITER_ID = USER.USER_ID
GROUP BY BOARD.WRITER_ID
HAVING sum(BOARD.PRICE)>=700000
ORDER BY TOTAL_SALES;