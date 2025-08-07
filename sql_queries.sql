-- 各廣告渠道營收、花費及 ROAS
SELECT MarketingChannel,
       SUM(Revenue) AS TotalRevenue,
       SUM(MarketingCost) AS TotalCost,
       ROUND(SUM(Revenue)/NULLIF(SUM(MarketingCost),0), 2) AS ROAS
FROM foodpanda_sales
GROUP BY MarketingChannel
ORDER BY ROAS DESC;
