-- script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;