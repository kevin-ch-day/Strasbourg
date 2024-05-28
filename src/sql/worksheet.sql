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
WHERE CompanyID = 11
    AND date BETWEEN '2021-04-03' AND DATE_ADD('2021-04-03', INTERVAL 7 DAY);

SELECT x.Date,
       x.Open AS 'Stock Open',
       x.Close AS 'Stock Close',
       x.Volume AS 'Stock Volume',
       y.Open AS 'Dow Jones Open',
       y.Close AS 'Dow Jones Close',
       y.Volume AS 'Dow Jones Volume'
FROM stock_data x
JOIN dow_jones y ON y.Date = x.Date
WHERE x.CompanyID = 22
    AND x.Date = '5/31/2021'
ORDER BY x.Date;

SELECT x.Date,
       x.Open AS 'Stock Open',
       x.Close AS 'Stock Close',
       x.Volume AS 'Stock Volume',
       y.Open AS 'Dow Jones Open',
       y.Close AS 'Dow Jones Close',
       y.Volume AS 'Dow Jones Volume'
FROM stock_data x
    LEFT JOIN dow_jones y
        ON y.Date = x.Date
WHERE x.CompanyID = 22
    AND x.Date BETWEEN '2021-05-25' AND '2021-06-07'
ORDER BY x.Date;

-- delete stock data by company id
DELETE FROM stock_data
WHERE CompanyID = 22;

-- Search for Disclosure Dates by company id
SELECT y.CompanyID as 'ID',
	y.CompanyName as 'Name',
    y.StockSymbol as 'Stock',
    x.DisclosureDate as 'Disclosure',
    x.Description,
    x.Impact
FROM data_breach_disclosures x
join company_info y
	on y.CompanyID = x.CompanyID
where y.CompanyID = 17