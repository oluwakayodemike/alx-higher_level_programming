-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each other.

SELECT g.name AS genre, COUNT(DISTINCT tsg.tv_show_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.name
HAVING COUNT(DISTINCT tsg.tv_show_id) > 0
ORDER BY number_of_shows DESC;

