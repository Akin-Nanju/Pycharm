SELECT employee_name, sale_amount,
       ROW_NUMBER() OVER(ORDER BY sales.sale_amount DESC) AS row_num
FROM sales;

SELECT *,
    ROW_NUMBER() OVER() AS ROW
FROM sales;

SELECT *,
    RANK() OVER(PARTITION BY sales.department ORDER BY sale_amount desc ) as Rnl
FROM sales;


SELECT *,
    dense_rank()OVER(PARTITION BY sales.department ORDER BY sale_amount desc ) as Rnl
FROM sales;

SELECT  *,
    NTILE(4) OVER (PARTITION BY department ORDER BY sale_amount DESC) AS ntile
FROM sales;

SELECT sales.department,
       AVG(sale_amount) OVER(PARTITION BY sales.department) as average
FROM sales;

SELECT *,
       SUM(sale_amount) OVER(PARTITION BY sales.department) as total
FROM sales;


--UNBOUNDED PRECIDING AND UNBOUNDED FOLLOWING - entire partition
--UNBOUNDED PRECIDING AND CURRENT ROW - from the start of the partition to the current row
--CURRENT ROW AND UNBOUNDED FOLLOWING - from the current row to the end of the partition
--BETWEEN 1 PRECEDING AND 1 FOLLOWING - from one row before the current row to one row after the current row
SELECT *
FROM (
    SELECT *
           SUM(sale_amount) OVER(PARTITION BY sales.department ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total
    FROM sales
) AS subquery
WHERE department = 'Electronics';



SELECT *
FROM(
    SELECT *,
        SUM(sale_amount) OVER(PARTITION BY department ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as total
    FROM sales
    ) AS subquery