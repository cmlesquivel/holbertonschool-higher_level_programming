-- script that lists all records of the table second_table where NULL dont' be
SELECT score, name
FROM second_table
WHERE name <> NULL
ORDER BY score DESC;
