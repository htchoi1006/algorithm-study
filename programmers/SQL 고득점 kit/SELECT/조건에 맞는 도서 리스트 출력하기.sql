SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY LIKE '인문' AND SUBSTR(PUBLISHED_DATE, 1, 4) = '2021'
ORDER BY BOOK_ID, PUBLISHED_DATE