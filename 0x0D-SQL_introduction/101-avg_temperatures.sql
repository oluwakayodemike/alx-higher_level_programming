-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT t.city, AVG(t.value) AS avg_temp
FROM temperatures AS t
GROUP BY t.city
ORDER BY avg_temp DESC;

