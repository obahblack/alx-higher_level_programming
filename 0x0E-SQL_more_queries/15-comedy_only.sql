-- script that list all comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_show.title
-- results must be sorted in ascending order by the show title
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
