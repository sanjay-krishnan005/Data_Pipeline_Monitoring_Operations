-- Total revenue

SELECT
    SUM(amount) AS total_revenue
FROM sales
WHERE amount >= 0;


-- Revenue by country

SELECT
    country,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_transaction
FROM sales
WHERE amount >= 0
GROUP BY country
ORDER BY total_revenue DESC;


-- Revenue by product

SELECT
    product,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_revenue
FROM sales
WHERE amount >= 0
GROUP BY product
ORDER BY total_revenue DESC;