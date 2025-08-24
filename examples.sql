USE  air_quality;

-- 1. Get the overall average PM2.5 level across all stations
SELECT AVG(pm25) AS avg_pm25
FROM mumbai_air_quality_clean;

-- 2. Find the top 5 most polluted days by PM2.5
SELECT date, station, pm25
FROM mumbai_air_quality_clean
ORDER BY pm25 DESC
LIMIT 5;

-- 3. Monthly average PM2.5 levels for trend analysis
SELECT DATE_TRUNC('month', date) AS month,
       ROUND(AVG(pm25), 2) AS avg_pm25
FROM mumbai_air_quality_clean
GROUP BY month
ORDER BY month;

-- 4. Station-wise average PM2.5 (to identify hotspots in Mumbai)
SELECT station,
       ROUND(AVG(pm25), 2) AS avg_pm25
FROM mumbai_air_quality_clean
GROUP BY station
ORDER BY avg_pm25 DESC;

-- 5. Categorize days based on PM2.5 pollution level
SELECT date,
       station,
       pm25,
       CASE
           WHEN pm25 <= 30 THEN 'Good'
           WHEN pm25 <= 60 THEN 'Satisfactory'
           WHEN pm25 <= 90 THEN 'Moderate'
           WHEN pm25 <= 120 THEN 'Poor'
           WHEN pm25 <= 250 THEN 'Very Poor'
           ELSE 'Severe'
       END AS pm25_category
FROM mumbai_air_quality_clean;

-- 6. Count of days in each air quality category (city-level)
SELECT pm25_category,
       COUNT(*) AS days_count
FROM (
    SELECT CASE
               WHEN pm25 <= 30 THEN 'Good'
               WHEN pm25 <= 60 THEN 'Satisfactory'
               WHEN pm25 <= 90 THEN 'Moderate'
               WHEN pm25 <= 120 THEN 'Poor'
               WHEN pm25 <= 250 THEN 'Very Poor'
               ELSE 'Severe'
           END AS pm25_category
		FROM mumbai_air_quality_clean
) 
GROUP BY pm25_category
ORDER BY days_count DESC;

-- 7. Identify seasonal pollution patterns (Quarterly average)
SELECT EXTRACT(YEAR FROM date) AS year,
       EXTRACT(QUARTER FROM date) AS quarter,
       ROUND(AVG(pm25), 2) AS avg_pm25
FROM mumbai_air_quality_clean
GROUP BY year, quarter
ORDER BY year, quarter;

-- 8. Correlation analysis proxy: compare PM2.5 and NO2
SELECT ROUND(CORR(pm25, no2), 3) AS correlation_pm25_no2
FROM mumbai_air_quality_clean;



