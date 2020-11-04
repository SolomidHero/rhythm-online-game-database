-- 1. Max рейтинг за сложность с id = 11 у юзера с id = 28
SELECT MAX(pp) as max_pp
FROM game.score as score
WHERE score.diff_id = 11 AND score.user_id = 28;

-- 2. Все карты юзера, в которые он играл
SELECT diff_id, MAX(pp) as max_pp
FROM game.score as score
WHERE score.user_id = 28
GROUP BY diff_id
ORDER BY max_pp DESC;

-- 3. Рейтинг пользователя с id = 28 на основании всех его карт
SELECT SUM(max_pp_table.max_pp) as rating
FROM (
    SELECT diff_id, MAX(pp) as max_pp
    FROM game.score as score
    WHERE score.user_id = 28
    GROUP BY diff_id
    ORDER BY max_pp DESC
) as max_pp_table;

-- 4. Рейтинги всех пользователей
SELECT u.username, coalesce(SUM(st.pp), 0) as rating
FROM game.UserProfile as u
LEFT JOIN (
    SELECT diff_id, user_id, MAX(pp) as pp
    FROM game.Score
    GROUP BY diff_id, user_id
) as st ON st.user_id = u.user_id
LEFT JOIN game.Difficulty ON st.diff_id = Difficulty.diff_id
GROUP BY u.username

-- 5. Сколько раз сыграли ту или иную сложность
SELECT dt.diff_id, coalesce(p.cnt, 0) as cnt
FROM game.Difficulty as dt
LEFT JOIN (
    SELECT st.diff_id as diff_id, count(*) as cnt 
    FROM game.Difficulty as dt
    LEFT JOIN game.score as st ON st.diff_id = dt.diff_id
    GROUP BY st.diff_id
) as p ON p.diff_id = dt.diff_id
ORDER BY cnt DESC;

-- 6. Сколько раз сыграли ту или иную песню
WITH diff_freq as (
    SELECT dt.map_id as map_id, coalesce(p.cnt, 0) as cnt
    FROM game.Difficulty as dt
    LEFT JOIN (
        SELECT st.diff_id as diff_id, count(*) as cnt 
        FROM game.Difficulty as dt
        LEFT JOIN game.score as st ON st.diff_id = dt.diff_id
        GROUP BY st.diff_id
    ) as p ON p.diff_id = dt.diff_id
    ORDER BY cnt DESC
)

SELECT bm.song, SUM(df.cnt) as cnt
FROM diff_freq as df
LEFT JOIN game.beatmap as bm ON bm.map_id = df.map_id
GROUP BY bm.song
ORDER BY cnt DESC;

-- 7.
SELECT p.map_id, avg(user_rating) OVER w
FROM (
    SELECT bmr.user_rating as user_rating, bmr.map_id
    FROM game.Beatmap as bm
    JOIN game.BeatmapRate as bmr ON bm.map_id = bmr.map_id
) as p
WINDOW w as (
    PARTITION BY p.map_id
);