-- lists the 'score' and number of occurance with each score with 'number'
-- displays this data sorted by number in desc order

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
