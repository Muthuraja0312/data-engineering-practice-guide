WITH cte AS
(
    SELECT *,
           ROW_NUMBER() OVER(
               PARTITION BY Company
               ORDER BY Salary
           ) rn,
           COUNT(*) OVER(
               PARTITION BY Company
           ) cnt
    FROM empk
)
SELECT Id, Company, Salary
FROM cte
WHERE rn BETWEEN cnt / 2.0
             AND cnt / 2.0 + 1;
