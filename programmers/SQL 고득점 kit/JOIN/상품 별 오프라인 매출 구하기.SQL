SELECT PRODUCT_CODE, SUM(SALES_AMOUNT*PRICE)AS SALES
FROM PRODUCT AS A 
JOIN OFFLINE_SALE AS B 
ON A.PRODUCT_ID = B.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC