-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT g.name AS genre, 
       COUNT(sg.tv_show_id) AS number_of_shows
FROM tv_genres g
LEFT JOIN (
    SELECT tv_show_id, tv_genre_id
    FROM tv_show_genres
) sg ON g.id = sg.tv_genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;

