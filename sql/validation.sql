-- Check missing customer IDs
SELECT *
FROM sales
WHERE customer_id IS NULL;


-- Check invalid amounts
SELECT *
FROM sales
WHERE amount < 0;


-- Check missing/invalid dates
SELECT *
FROM sales
WHERE transaction_date IS NULL;


-- Check duplicate transactions
SELECT
    transaction_id,
    COUNT(*) AS record_count
FROM sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;