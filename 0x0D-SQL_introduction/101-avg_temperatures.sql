-- Task 18
-- Script displays the average tempature by city ordered by tempature
SELECT DISTINCT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
