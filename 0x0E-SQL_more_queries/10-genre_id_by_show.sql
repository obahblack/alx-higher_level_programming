-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- a script that list all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Each record should display: tv_show.title, tv_show_genres.genre_id
-- Result must be sorted in ascending order by tv_show.title and tv_show_genres.genre_id
-- you can only use one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
