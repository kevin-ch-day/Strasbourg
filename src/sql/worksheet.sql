SELECT x.Date, COUNT(x.Date) > 0 AS HasStockData
FROM stock_data x
LEFT JOIN dow_jones y 
    ON y.Date = x.Date
WHERE x.CompanyID = 11 
    AND x.Date IN ('2018-09-28', '2019-04-03', '2021-04-03')
GROUP BY x.Date
ORDER BY x.Date;


SELECT *
FROM stock_data
WHERE CompanyID = 11 AND date BETWEEN '2021-04-03' AND DATE_ADD('2021-04-03', INTERVAL 7 DAY);
