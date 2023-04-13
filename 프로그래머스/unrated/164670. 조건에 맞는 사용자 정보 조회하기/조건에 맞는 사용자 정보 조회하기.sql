SELECT USER.USER_ID, USER.NICKNAME, CONCAT(CITY,' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소', 
CONCAT(LEFT(tlno,3),"-",SUBSTR(tlno,4,4),"-",RIGHT(tlno,4)) AS '전화번호'
# , COUNT(BOARD.BOARD_ID)
FROM USED_GOODS_BOARD AS BOARD
INNER JOIN USED_GOODS_USER AS USER
ON BOARD.WRITER_ID = USER.USER_ID
GROUP BY USER.USER_ID
HAVING COUNT(BOARD.BOARD_ID) > 2
ORDER BY USER.USER_ID DESC