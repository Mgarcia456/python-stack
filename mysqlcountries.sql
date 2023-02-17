--  first query
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
-- second query 
SELECT countries.name, COUNT(*) FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(*) DESC;
-- third query
SELECT cities.name, countries.name, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;
-- fourth query
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
-- fifth query 
SELECT countries.name, countries.surface_area, countries.population FROM COUNTRIES
WHERE countries.surface_area < 501 and countries.population > 100000;
-- sixth query
SELECT countries.name, countries.government_form, countries.capital, 
countries.life_expectancy from countries
WHERE countries.government_form = 'Constitutional Monarchy' 
AND countries.capitals > 200
AND countries.life_expectancy > 75
GROUP BY countries.name;
-- seventh query
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;
-- last query
SELECT countries.region, COUNT(*)
FROM countries
GROUP BY countries.region
ORDER BY COUNT(*) DESC;
